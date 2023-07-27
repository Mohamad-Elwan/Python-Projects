"""
Sysadmintask.py
Creates a file and sends it to the server.
Monty Albobsairy, Mohamed Elwan
"""
import socket
import os
import pwd
import grp
import json

SERVER_IP = '192.168.1.5'
SERVER_PORT = 5000
BUFFER_SIZE = 1024
JSON_FILE = 'Cpu_info.json'


def get_computer_name():
    """Get the current computer name."""
    return socket.gethostname()


def get_names_and_groups():
    """
    Get a list of account names and their groups.
    For each account, it retrieves the default group and checks if the account is a member of any other groups.
    Returns a list of dictionaries with 'AccountName' and 'Groups'.
    """
    return [
        {"AccountName": account.pw_name, "Groups": [grp.getgrgid(account.pw_gid).gr_name] + [group.gr_name for group in grp.getgrall() if account.pw_name in group.gr_mem]}
        for account in pwd.getpwall()
    ]


def get_cpu_info():
    """
    Get CPU information from /proc/cpuinfo.
    Reads the file and filters lines containing the desired keywords.
    Returns a list of CPU information lines.
    """
    try:
        with open('/proc/cpuinfo', 'r') as file_ref:
            return [line.strip() for line in file_ref if any(keyword in line for keyword in ['vendor_id', 'model', 'model name', 'cache'])]
    except FileNotFoundError:
        print('Could not obtain /proc/cpuinfo')
        return []


def get_running_services():
    """
    Get a list of running services.
    Executes the systemctl command to list running services and extracts the service names.
    Returns a list of running service names.
    """
    return [service.split()[0] for service in os.popen('systemctl list-units --type=service --no-pager --no-legend').read().splitlines()]


def create_info_dictionary():
    """
    Create a dictionary with computer information.
    Calls the helper functions to obtain computer name, account names and groups, CPU information, and running services.
    Returns a dictionary containing the computer information.
    """
    return {
        "ComputerName": get_computer_name(),
        "AccountTable": sorted(get_names_and_groups(), key=lambda x: x['AccountName'].lower()),
        "CpuInfo": get_cpu_info(),
        "RunningServices": get_running_services()
    }


def send_json_data():
    """
    Send JSON data to the server.
    Connects to the server using a socket, creates the JSON data using the create_info_dictionary() function,
    and sends it to the server.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))

    json_data = create_info_dictionary()
    client_socket.send(json.dumps(json_data).encode())

    client_socket.close()
    print("JSON data sent successfully.")


def receive_json_data():
    """
    Receive JSON data from the client.
    Binds the server socket to the IP and port, listens for incoming connections, accepts the client connection,
    receives the JSON data, decodes it, and prints the computer information.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(1)
    print("Waiting for a client connection...")

    connection, address = server_socket.accept()
    print("Connected to client:", address)

    received_data = connection.recv(BUFFER_SIZE)
    info_dictionary = json.loads(received_data.decode())

    print("JSON data received successfully.")
    print("Computer Name:", info_dictionary["ComputerName"])
    print("Account Table:", info_dictionary["AccountTable"])
    print("CPU Info:", info_dictionary["CpuInfo"])
    print("Running Services:", info_dictionary["RunningServices"])

    connection.close()
    server_socket.close()


def main():
    """
    Main function to handle server and client operations.
    Checks if the JSON file exists. If it does, assumes it is the server and receives JSON data.
    If the file does not exist, assumes it is the client and sends JSON data.
    Finally, if it is the client, writes the JSON data to a file.
    """
    if os.path.exists(JSON_FILE):
        receive_json_data()
    else:
        send_json_data()
        with open(JSON_FILE, 'w') as json_file:
            json.dump(create_info_dictionary(), json_file, indent=2)

    print("Process completed.")


if __name__ == "__main__":
    main()
