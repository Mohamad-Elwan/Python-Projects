"""
Client.py
This Script uses socket to send a file using the servers ip address and the port it's using to receive the file. It takes
the file from the sysadmin script and sends it to the server.
Monty Albobsairy, Mohamed Elwan
July 16,2023
"""

import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
server_ip = "192.168.1.5"
server_port = 5000
client_socket.connect((server_ip, server_port))

# open the file to be sent
file_path = "/mohamad/home/log.txt"
with open(file_path, "rb") as file:
    # read the file in buffer of 1024 bytes
    line = file.read(1024)

    print("Sending file...")
    while line:
        # send each buffer to the server
        client_socket.send(line)
        line = file.read(1024)

# close the client socket
client_socket.close()

print("Finished sending file")
print("Connection closed")