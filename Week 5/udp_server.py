import sys
from socket import *

server_name = "10.0.2.15"
server_port = 12000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("", server_port))

print(f"Server 10.0.2.15 is ready to receive on port {server_port}")

while True:
    message, client_address = server_socket.recvfrom(2048)
    message = message.upper()
    server_socket.sendto(message, client_address)