import socket, os
import json_protocol as prot

HOST = '127.0.0.1'
PORT = 8000
ADDR = (HOST, PORT)


if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(ADDR)
    server_socket.listen(5)

    print(f'Server listening on {HOST}:{PORT}')
    client_socket, client_addr = server_socket.accept()
    print(f'Client connected from {client_addr}')

    while True:
        try:
            file_name = prot.recv_all(socket=client_socket)
            if file_name == '':
                raise ConnectionResetError('Client has disconnected')

        except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError) as e:
            print(f"Unexpected error with {client_addr}: {e}")
            print(f'Server listening on {HOST}:{PORT}')
            client_socket, client_addr = server_socket.accept()
            print(f'Client connected from {client_addr}')
            continue

        if file_name != '':
            os.startfile(file_name)

    server_socket.close()
    client_socket.close()
    input()