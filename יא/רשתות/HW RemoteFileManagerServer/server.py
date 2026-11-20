from datetime import datetime
import socket, os
import protocol as prot

HOST = '127.0.0.1'
PORT = 8000
ADDR = (HOST, PORT)
dir = "server_storage"

def find_dirpath(dir,dir_name):
    dir_path = ""
    for root, dirs, files in os.walk(dir):
        if dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
    return dir_path

def find_filepath(dir, file_name):
    file_path = ""
    for root, dirs, files in os.walk(dir):
        if file_name in files:
            file_path = os.path.join(root, file_name)
    return file_path

def str_from_dir(dir):
    dir_str = ""
    for item in os.listdir(dir):
        if os.path.isdir(fr"{dir}\{item}"):
            dir_str+= f"DIR: {item},"
        else:
            dir_str+= f"FILE : {item},"

    return dir_str

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(ADDR)
    server_socket.listen(5)

    print(f'Server listening on {HOST}:{PORT}')
    client_socket, client_addr = server_socket.accept()
    print(f'Client connected from {client_addr}')

    while True:
        try:
            try:
                param, command = prot.recv_status(socket = client_socket)
            except ValueError:
                print("Client has disconnected")
                break

            if command == "UPLOAD":
                param = prot.recv_all(socket=client_socket)
                prot.send_status(socket = client_socket, file_name = param, command ="SUCCESS")

            if command == 'DOWNLOAD':
                file_path = find_filepath(dir, param)
                if prot.send_all(socket = client_socket , file_name = file_path , command = command) == "ERROR 404: FILE NOT FOUND":
                    prot.send_status(socket=client_socket, file_name=file_path, command="404")
                else:
                    prot.send_status(socket=client_socket, file_name=file_path, command="SUCCESS")

            if command == "DELETE":
                file_path = find_filepath(dir, param)
                if file_path != "":
                    os.remove(file_path)
                    prot.send_status(socket=client_socket, file_name=param, command="SUCCESS")
                else:
                    prot.send_status(socket=client_socket, file_name=param, command="404")

            if command == "DIR":
                if param == "":
                    dir_path = os.path.abspath(dir)
                else:
                    dir_path = find_dirpath(dir, param)

                if dir_path != "":
                    dir_str = str_from_dir(dir_path)
                    prot.send_message(socket= client_socket, data= dir_str)
                    prot.send_status(socket=client_socket, file_name=param, command="SUCCESS")
                else:
                    prot.send_status(socket=client_socket, file_name=param, command="404")

            if command == "INFO":
                file_path = find_filepath(dir, param)
                time = os.path.getmtime(file_path)
                time = datetime.fromtimestamp(time).strftime("%d-%m-%Y %H:%M:%S")
                size = os.path.getsize(file_path)
                if file_path != "":
                    prot.send_message(socket= client_socket, data= f"Size: {size}, Modified: {time}")
                    prot.send_status(socket=client_socket, file_name=param, command="SUCCESS")
                else:
                    prot.send_status(socket=client_socket, file_name=param, command="404")



        except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError) as e:
            print(f"Unexpected error with {client_addr}: {e}")
            print(f'Server listening on {HOST}:{PORT}')
            client_socket, client_addr = server_socket.accept()
            print(f'Client connected from {client_addr}')
            continue


    server_socket.close()
    client_socket.close()

