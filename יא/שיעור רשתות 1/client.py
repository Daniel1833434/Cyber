import socket
import protocol as prot

HOST = '127.0.0.1'
PORT = 8080
ADRR = (HOST, PORT)

if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Connecting to server {HOST}:{PORT}")
    client_socket.connect(ADRR)

    while True:
        user_input = input('>')
        while user_input == '':
            user_input = input('>')

        if user_input in ['quit','exit']:
            prot.send_all(data = 'quit')
            break
        #client_socket.send(user_input.encode())
        prot.send_all(data = user_input , socket = client_socket)
        #received_data = client_socket.recv(BUFSIZE).decode()
        recv_data = prot.recv_all(socket = client_socket)
        #print(f"received {received_data}")

    client_socket.close()