from socket import *

server_port = 12000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("", server_port))

print("The server is ready to receive...")

while True:
    message, client_address = server_socket.recvfrom(2048)
    message = message.upper()
    server_socket.sendto(message, client_address)