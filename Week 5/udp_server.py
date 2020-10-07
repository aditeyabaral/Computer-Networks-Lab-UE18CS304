import sys
from socket import socket, AF_INET, SOCK_DGRAM

server_name = "10.0.4.26"
server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind((server_name, server_port))

print(f"Server {server_name} is ready to receive on port {server_port}")

while True:
    message, client_address = server_socket.recvfrom(2048)
    message = message.upper()
    server_socket.sendto(message, client_address)