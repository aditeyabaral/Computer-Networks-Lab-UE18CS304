import os
import sys
import threading
from socket import socket, AF_INET, SOCK_STREAM, error

NUM_REQS = 50
BUF_SIZE = 999999


def proxy_server_thread(client_conn, client_addr):
    request = client_conn.recv(BUF_SIZE)
    request_first_line = request.decode().split("\n")[0]
    url = request_first_line.split(" ")[1]
    print("From", "\t", client_addr[0], "\t", "Request", "\t", request_first_line)

    http_pos = url.find("://")
    if http_pos == -1:
        temp = url
    else:
        temp = url[(http_pos + 3) :]

    port_pos = temp.find(":")

    webserver_pos = temp.find("/")
    if webserver_pos == -1:
        webserver_pos = len(temp)

    webserver = ""
    port = -1
    if port_pos == -1 or webserver_pos < port_pos:
        port = 80
        webserver = temp[:webserver_pos]
    else:
        port = int((temp[(port_pos + 1) :])[: webserver_pos - port_pos - 1])
        webserver = temp[:port_pos]

    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((webserver, port))
        s.send(request)
        while 1:
            response = s.recv(BUF_SIZE)
            response_first_line = response.decode("utf8", "ignore").partition("\n")[0]
            print(
                "To", "\t", client_addr[0], "\t", "Response", "\t", response_first_line
            )
            if len(response) > 0:
                client_conn.send(response)
            else:
                break
        s.close()
        client_conn.close()
    except error:
        if s:
            s.close()
        if client_conn:
            client_conn.close()
        print(client_addr[0], "\t", "Peer reset", "\t", request_first_line)
        sys.exit(1)


def proxy_server():
    if len(sys.argv) < 2:
        print("Using Default port 8080 since no port was mentioned.")
        port = 8080
    else:
        port = int(sys.argv[1])
    host = ""
    print("Proxy server Running on localhost :", port)
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.bind((host, port))
        s.listen(NUM_REQS)
    except error:
        if s:
            s.close()
        print("Could not open socket:")
        sys.exit(1)
    while 1:
        client_conn, client_addr = s.accept()
        threading._start_new_thread(proxy_server_thread, (client_conn, client_addr))
    s.close()


if __name__ == "__main__":
    proxy_server()
