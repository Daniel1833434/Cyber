import socket
import protocol as prot

HOST = '127.0.0.1'
PORT = 8000
ADDR = (HOST, PORT)


if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f'[CONNECTING TO SERVER] {ADDR}')
    client_socket.connect(ADDR)

    with open("math_exe.txt", encoding="utf-8-sig") as file , open("math_answers.txt","w",encoding="utf-8-sig") as file2:
        for line in file:
            mathproblem = line.strip()
            prot.send_all(socket=client_socket, data=mathproblem)
            recv_data = prot.recv_all(socket=client_socket)
            file2.write(recv_data + "\n")
    prot.send_all(socket=client_socket, data='quit')
    client_socket.close()
