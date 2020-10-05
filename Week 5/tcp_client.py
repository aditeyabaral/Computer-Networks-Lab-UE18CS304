from socket import *

server_name = "host"
server_port = 12000
client_socket = socket (AF_INET, SOCK_STREAM)
client_socket.connect(server_name, server_port)

sentence = input("Enter sentence: ")
client_socket.send(sentence)
modified_sentence = client_socket.recv(1024)
print(f"server > {modified_sentence}")
client_socket.close()