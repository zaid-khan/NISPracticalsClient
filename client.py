#!/usr/bin/env python3

import socket

#HOST = '127.0.0.1'  # The server's hostname or IP address
def send_data_to_server(my_str):
    HOST = '127.0.0.1'
    PORT = 30000        # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(my_str.encode('utf-8'))
        # data = s.recv(1024)

    # print('Received', repr(data))
