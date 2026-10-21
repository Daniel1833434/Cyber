import socket

HOST = '127.0.0.1'
PORT = 8080
ADRR = (HOST, PORT)
BUFSIZE = 1024

if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Connecting to server {HOST}:{PORT}")
    client_socket.connect(ADRR)

    while True:
        user_input = input('>')
        client_socket.send(user_input.encode())
        received_data = client_socket.recv(BUFSIZE).decode()
        print(f"received {received_data}")