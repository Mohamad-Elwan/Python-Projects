'''
Project_3_pywin32.py

This scripts check for CPU and Memory usage every 2 hours and log the information into a text file for future
analysis. It also logs out a user after a specific time of inactivity in windows and writes to a file. Also, it
obtains system information like users, groups they belong to, IP addresses and prints it out to the screen formatted.

Montedher Albobsairy, Mohamed Elwan
'''
import win32process, datetime, time, win32api, win32console, win32con, win32com.client


# Mohamad Elwan July 03/2023
# This is the log data functions to create a log file and log system monitoring data and time occurs
def log_data(data):
    log_file_path = "windows_system_monitoring_log.txt"
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{current_time}] CPU Usage: {data['cpu_usage']}%, Memory Usage: {data['memory_usage']} bytes"

    try:
        with open(log_file_path, "a") as log_file:
            log_file.write(log_message + "\n")
    except:
        print('Error writing to log file')


# This function monitor the computer and writes down the information
def monitor_system(interval, log_interval):
    start_time = time.time()
    next_log_time = start_time + log_interval

    while True:
        current_time = time.time()

        if current_time >= next_log_time:
            cpu_times = win32process.GetProcessTimes(win32process.GetCurrentProcess())
            kernel_time = cpu_times["KernelTime"]
            user_time = cpu_times["UserTime"]
            total_time = kernel_time + user_time
            cpu_usage = (total_time / (time.time() - start_time)) * 100
            memory_usage = win32process.GetProcessMemoryInfo(win32process.GetCurrentProcess())["WorkingSetSize"]

            data = {
                "cpu_usage": cpu_usage,
                "memory_usage": memory_usage,
            }
            log_data(data)

            next_log_time = current_time + log_interval

        time.sleep(interval)


# This function sets how often we want to check the system and write down information.
def main():
    # interval and log_interval are in seconds
    interval = 2  # This timer is checking time between each system monitoring check
    log_interval = 2  # this time in seconds for when every time system monitoring checks and log
    # This tells us if the system not working and tells that there is an error
    try:
        monitor_system(interval, log_interval)
    except:
        print("An error occurred")


'''
This Part logs out a user after a specific time of inactivity in windows and logs it out in a text file
'''


def log_event(event_type):
    log_file_path = "user_activity_log.txt"

    # Gets the current timestamp
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")

    # This functions logs event and time
    log_message = f"[{current_time}] Event: {event_type}"
    with open(log_file_path, "a") as log_file:
        log_file.write(log_message + "\n")


def check_user_activity(timeout):
    # this timer is in seconds
    shutdown_timeout = 30

    while True:
        # checks for the time of last user activity
        last_input_tick = win32api.GetLastInputInfo()

        # checks for computer current run time
        current_tick = win32api.GetTickCount()

        # compute the time since the last user input
        process_time = current_tick - last_input_tick

        # This function logs out the user if there is no activity for a specific time
        if process_time > timeout:
            # in line 20 we have beep sound function, so it make a sound before logging out user
            win32api.MessageBeep(win32con.MB_OK)
            log_event("User Logoff")
            win32console.FreeConsole()
            win32api.ExitWindowsEx(win32con.EWX_LOGOFF)
            break


"""
A divider function that iterates between ~ and - to print out a line that is used to divide sections of text later in this code.
"""


def Divider():
    length = range(100)
    for character in length:
        if character % 2 == 0:
            print('~', end='')
        else:
            print('-', end='')
    print()


"""The function that uses wincom.client to obtain network information, cpu information and account information. It 
creates a dictionary to store accounts and is in a for loop to map them together with their groups. For network 
information it uses IPAddress, DefaultIPGateway and IPSubnet to get those values. It then prints it out to 
the screen using the divider function to make it look nice and readable"""


def get_system_information():
    wmi = win32com.client.GetObject("winmgmts:")
    network_configs = wmi.InstancesOf("Win32_NetworkAdapterConfiguration")
    cpu_info = wmi.ExecQuery("SELECT * FROM Win32_Processor")
    user_accounts = wmi.InstancesOf("Win32_UserAccount")
    group_membership = wmi.InstancesOf("Win32_GroupUser")

    group_mapping = {}
    for group in group_membership:
        group_component = group.GroupComponent
        user_component = group.PartComponent
        group_name = group_component.split('Name=')[1].split(',')[0]
        user_name = user_component.split('Name=')[1].split(',')[0]

        if user_name not in group_mapping:
            group_mapping[user_name] = []
        group_mapping[user_name].append(group_name)

    Divider()
    print('Network Information'.upper())
    Divider()
    for config in network_configs:
        if config.IPEnabled:
            ip_addresses = config.IPAddress
            default_gateway = config.DefaultIPGateway[0] if config.DefaultIPGateway else ""
            subnet_masks = config.IPSubnet

            print('IP Addresses: ' + str(ip_addresses) + "\n" + 'Subnet Mask: ' + str(subnet_masks) + "\n" + 'Default '
                                                                                                             'Gateway: ' + default_gateway)

    for cpu in cpu_info:
        Divider()
        print('CPU Information'.upper())
        Divider()
        print(
            'Name: ' + cpu.Name + "\n" + 'Manufacturer: ' + cpu.Manufacturer + "\n" + 'Number Of Cores: ' + str(
                cpu.NumberOfCores))

    Divider()
    print('Accounts & Details'.upper())
    Divider()
    for account in user_accounts:
        username = account.Name
        full_name = account.FullName
        groups = group_mapping.get(username, [])
        groups_formatted = ', '.join(groups)
        print(
            'Username: ' + username + "\n" + ' Full Name: ' + full_name + "\n" + ' Groups: ' + groups_formatted + "\n")
    Divider()

    return


# Prints out system information in uppercase and runs the function, Also where we call all the functions we've made.
Divider()
print("System Information:".upper())
get_system_information()

# timeout timer is in Milliseconds
timeout = 300000
check_user_activity(timeout)

if __name__ == "__main__":
    main()
