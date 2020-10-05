from socket import *

server_name = "host"
server_port = 12000
client_socket = socket (AF_INET, SOCK_STREAM)

sentence = input("Enter sentence: ")
client_socket.sendto(sentence, (server_name, server_port))
modified_sentence, server_address = client_socket.recv(2048)
print(f"server [{server_address}]> {modified_sentence}")
client_socket.close()