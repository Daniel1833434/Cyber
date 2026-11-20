import protocol as prot
import os

def UPLOAD(filename, client_socket):
    prot.send_status(command ="UPLOAD", file_name= filename, socket= client_socket)
    if not os.path.exists(filename):
        return "ERROR 404: FILE NOT FOUND"
    try:
        bytes_uploaded = prot.send_all(file_name = filename, socket = client_socket, command = "UPLOAD")
        if prot.recv_status(socket = client_socket)[1] == "SUCCESS":
            return f"200 SUCCESS({bytes_uploaded} bytes uploaded)"
    except:
        return "Unkown Error"

def DOWNLOAD(filename,client_socket):
    prot.send_status(command ="DOWNLOAD", file_name= filename, socket= client_socket)
    try:
        dir = prot.recv_all(socket= client_socket)
        status = prot.recv_status(socket=client_socket)[1]
        if status == "404":
            return "ERROR 404: FILE NOT FOUND"
        else:
            return f"200 SUCCESS (Saved to {dir})"
    except:
        return "Unkown Error"

def DELETE(filename,client_socket):
    prot.send_status(command ="DELETE", file_name= filename, socket= client_socket)
    try:
        status = prot.recv_status(socket=client_socket)[1]
        if status  == "SUCCESS":
            return "200 DELETED"
        elif status == "404":
            return "ERROR 404: FILE NOT FOUND"
    except:
        return "Unkown Error"

def DIR(directory,client_socket):
    prot.send_status(command ="DIR", file_name= directory, socket= client_socket)
    try:
        dir = prot.recv_message(socket= client_socket)
        status = prot.recv_status(socket=client_socket)[1]
        if status  == "SUCCESS":
            return f"200 SUCCESS ({dir})"
        elif status == "404":
            return "ERROR 404: DIR NOT FOUND"
    except:
        return "Unkown Error"

def INFO(filename,client_socket):
    prot.send_status(command="INFO", file_name=filename, socket=client_socket)
    try:
        info = prot.recv_message(socket= client_socket)
        status = prot.recv_status(socket=client_socket)[1]
        if status == "SUCCESS":
            return f"200 SUCCESS ({info})"
        elif status == "404":
            return "ERROR 404: FILE NOT FOUND"
    except:
        return "Unkown Error"
