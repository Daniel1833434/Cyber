import socket
import protocol as prot

HOST = '127.0.0.1'
PORT = 8000
ADDR = (HOST, PORT)


if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f'[CONNECTING TO SERVER] {ADDR}')
    client_socket.connect(ADDR)

    while True:
        user_input = input('enter string to send > ')
        while user_input == '':
            user_input = input('enter string to send > ')

        if user_input == 'quit':
            prot.send_all(socket=client_socket, data="quit")
            break

        # client_socket.send(user_input.encode())
        prot.send_all(socket=client_socket, data=user_input)
        # received_data = client_socket.recv(BUFSIZE).decode()
        recv_data = prot.recv_all(socket=client_socket)
        # print(f'received {received_data}')

    client_socket.close()