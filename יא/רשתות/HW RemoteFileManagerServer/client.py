import socket, os
import protocol as prot
import functions as functions

HOST = '127.0.0.1'
PORT = 8000
ADDR = (HOST, PORT)


if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f'[CONNECTING TO SERVER] {ADDR}')
    client_socket.connect(ADDR)

    with open("file_commands.txt", encoding="utf-8-sig") as commands , open("manager_log.txt","w",encoding="utf-8-sig") as log:
        for line in commands:
            line = line.strip()
            if line == "":
                continue
            try:
                command,param = line.split(":",1)
            except ValueError:
                log.write(f"{line} = ERROR 400: INVALID COMMAND \n")
                continue

            result = ""
            if command == 'UPLOAD':
                result = functions.UPLOAD(param,client_socket)
            elif command == 'DOWNLOAD':
                result = functions.DOWNLOAD(param,client_socket)
            elif command == "DELETE":
                result = functions.DELETE(param,client_socket)
            elif command == "DIR":
                result = functions.DIR(param,client_socket)
            elif command == "INFO":
                result = functions.INFO(param,client_socket)
            else:
                result = functions.INVALID_COMMAND(param,client_socket,command)

            log.write(f"{command}:{param} = {result} \n")

    client_socket.close()
