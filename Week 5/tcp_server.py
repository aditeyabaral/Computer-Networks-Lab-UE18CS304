from socket import *

server_name = "10.0.2.15"
server_port = 12000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((server_name, server_port))
server_socket.listen(1)

print(f"Server 10.0.2.15 is ready to receive on port {server_port}")

while True:
    connection_socket, address = server_socket.accept()
    sentence = connection_socket.recv(1024)
    sentence = sentence.upper()
    connection_socket.send(sentence)
    connection_socket.close()