import sys
from socket import socket, AF_INET, SOCK_DGRAM

server_name = sys.argv[1].encode()
server_port = int(sys.argv[2])
client_socket = socket(AF_INET, SOCK_DGRAM)

sentence = input("\nEnter sentence: ").encode()
client_socket.sendto(sentence, (server_name, server_port))
modified_sentence, server_address = client_socket.recvfrom(2048)
print(f"{server_address[0]} > {modified_sentence.decode()}")
client_socket.close()
