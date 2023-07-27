"""
Server.py
This Script uses socket to receive a file while listening to all network interfaces on a specified port. It then saves it
to wherever specified.
Monty Albobsairy, Mohamed Elwan
July 16,2023
"""




import socket

Host = '0.0.0.0'  # listen on all available network interfaces
Port = 5000  # port number


def receive_file(connection):
    # receive the file data from the client
    file_data = connection.recv(1024)

    # save the file to specified directory
    file_path = 'C:/Monty Extras/received_file.txt'
    with open(file_path, 'wb') as file:
        file.write(file_data)

    print(f"Received file saved: {file_path}")


# starts the server and listens on the host and port specified at the top. Once connected it will close.
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((Host, Port))
        server_socket.listen(1)
        print(f"Server listening on {Host}:{Port}")

        while True:
            connection, address = server_socket.accept()
            print(f"Connection established from: {address[0]}:{address[1]}")

            receive_file(connection)
            connection.close()


if __name__ == '__main__':
    start_server()
