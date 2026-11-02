import socket, os
import file_protocol as prot

HOST = '127.0.0.1'
PORT = 8000
ADDR = (HOST, PORT)


if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f'[CONNECTING TO SERVER] {ADDR}')
    client_socket.connect(ADDR)

    while True:
        try:
            user_input = input('enter file name > ')
            if not os.path.exists(user_input):
                print('No Such File...')
                continue

            prot.send_all(socket=client_socket, file_name=user_input)
        except Exception as e:
            print(e)
            break

    client_socket.close()