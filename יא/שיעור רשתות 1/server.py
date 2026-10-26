import socket
import protocol as prot

HOST = '127.0.0.1'
PORT = 8080
ADRR = (HOST, PORT)

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(ADRR)
    server_socket.listen(5)
    print(f'Server listening at {HOST}:{PORT}')
    client_socket, client_addr = server_socket.accept()
    print(f'Client connected from {client_addr}')
    while True:
        #data = client_socket.recv(BUFSIZE)
        data = prot.recv_all(socket = client_socket)
        if data == "":
            print("Client disconnected from server")
            print(f'Server listening at {HOST}:{PORT}')
            client_socket, client_addr = server_socket.accept()
            print(f'Client connected from {client_addr}')
            continue

        if data in ['quit','exit']:
            break

        # print(f"Received {data}")
        # client_socket.sendall(data)
        prot.send_all(data = data, socket = client_socket)

    server_socket.close()
    client_socket.close()