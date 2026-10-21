import socket

HOST = '127.0.0.1'
PORT = 8080
ADRR = (HOST, PORT)
BUFSIZE = 1024

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(ADRR)
    server_socket.listen(5)
    print(f'Server listening at {HOST}:{PORT}')
    client_socket, client_addr = server_socket.accept()
    print(f'Client connected from {client_addr}')
    while True:
        data = client_socket.recv(BUFSIZE)
        if data.decode() == "":
            print("Client disconnected from server")
            print(f'Server listening at {HOST}:{PORT}')
            client_socket, client_addr = server_socket.accept()
            print(f'Client connected from {client_addr}')
            continue
        if data.decode() in ['quit','exit']:
            client_socket.close()
            break

        print(f"Received {data.decode()}")
        client_socket.sendall(data)

    server_socket.close()
    client_socket.close()