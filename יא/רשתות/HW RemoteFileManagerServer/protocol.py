import json
import os
from tqdm import tqdm
BUFSIZE = 2048
HEADER_LEN = 6

def recv_message(**kwargs):
    client_socket = kwargs.get('socket')
    recv_data = b''
    msg_len = client_socket.recv(HEADER_LEN).decode()

    if msg_len == '':
        return ''

    msg_len = int(msg_len)

    while len(recv_data) < msg_len:
        recv_data += client_socket.recv(min(BUFSIZE,msg_len-len(recv_data)))

    print(f"received {recv_data.decode()}")
    return recv_data.decode()

def send_message(**kwargs):
    data = kwargs.get('data', "ERROR No Data Received")
    client_socket = kwargs.get('socket')
    msg_len = str(len(data)).rjust(HEADER_LEN, '0')
    send_msg = msg_len + data
    client_socket.send(send_msg.encode())
    print(f"sent {send_msg}")

def recv_status(**kwargs):
    client_socket = kwargs.get('socket')

    json_obj_len = client_socket.recv(HEADER_LEN).decode()

    if json_obj_len == '':
        return ''

    json_obj_str = client_socket.recv(int(json_obj_len)).decode()
    json_obj = json.loads(json_obj_str)

    file_name = json_obj["file_name"]
    command = json_obj["command"]

    return file_name,command

def send_status(**kwargs):
    command = kwargs.get('command')
    file_name = kwargs.get("file_name")
    client_socket = kwargs.get('socket')

    json_obj = {
        "file_name": file_name,
        "command": command
    }
    json_str = json.dumps(json_obj)
    client_socket.send(str(len(json_str)).rjust(HEADER_LEN, '0').encode())
    client_socket.send(json_str.encode())

def recv_all(**kwargs):
    client_socket = kwargs.get('socket')

    json_obj_len = client_socket.recv(HEADER_LEN).decode()

    if json_obj_len == '':
        return ''

    json_obj_str  = client_socket.recv(int(json_obj_len)).decode()
    json_obj = json.loads(json_obj_str)

    file_name = json_obj["file_name"]
    file_size = json_obj["file_size"]
    command = json_obj["command"]

    dir = fr'server_storage\server_download' if command == "UPLOAD" else "client_downloads"
    if not os.path.exists(dir):
        os.mkdir(dir)

    cwd = os.getcwd()
    file = open(fr"{cwd}\{dir}\{file_name}", 'wb')

    msg_len = int(file_size)
    print('Begin Receiving File...')
    byte_count = 0

    with tqdm(total=msg_len, desc="Processing") as pbar:
        while byte_count < msg_len:
            image_chunk = client_socket.recv(min(BUFSIZE,msg_len-byte_count))
            file.write(image_chunk)
            byte_count += len(image_chunk)
            pbar.n = byte_count
            pbar.refresh()

    print(f"{file_name.strip()}, {byte_count} bytes uploaded successfully")
    file.close()
    return fr"{cwd}\{dir}\{file_name}"

def send_all(**kwargs):
    client_socket = kwargs.get('socket')
    file_name = kwargs.get('file_name')
    command = kwargs.get('command')
    if not os.path.exists(file_name):
        return "ERROR 404: FILE NOT FOUND"
    file = open(file_name, 'rb')
    file_size = str(os.path.getsize(file_name))
    json_obj = {
        "file_name": os.path.basename(file_name),
        "file_size": file_size,
        "command" : command
    }
    json_str = json.dumps(json_obj)
    client_socket.send(str(len(json_str)).rjust(HEADER_LEN,'0').encode())
    client_socket.send(json_str.encode())

    image_data = 0
    print(f'Begin Sending {file_name.strip()} ...')
    file_size = int(file_size)
    with tqdm(total=file_size, desc="Processing") as pbar:
        while image_data < file_size:
            rxd = file.read(BUFSIZE)
            image_data += len(rxd)
            client_socket.send(rxd)
            pbar.n = image_data
            pbar.refresh()

    print(f'{file_name.strip()},  {file_size} bytes Sent Successfully...')
    file.close()
    return file_size
