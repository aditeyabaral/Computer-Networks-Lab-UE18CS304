import sys
from socket import socket, AF_INET, SOCK_STREAM

server_name = sys.argv[1].encode()
server_port = int(sys.argv[2])
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))

sentence = input("\nEnter sentence: ").encode()
client_socket.send(sentence)
modified_sentence = client_socket.recv(1024)
print(f"{server_name.decode()} > {modified_sentence.decode()}")
client_socket.close()
