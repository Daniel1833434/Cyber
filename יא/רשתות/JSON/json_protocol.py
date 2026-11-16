import json
import os
from tqdm import tqdm
import json
BUFSIZE = 2048
HEADER_LEN = 6


def recv_all(**kwargs):
    client_socket = kwargs.get('socket')
    # first receive file name
    json_obj_len = client_socket.recv(HEADER_LEN).decode()

    if json_obj_len == '':
        return ''

    json_obj_str  = client_socket.recv(int(json_obj_len)).decode()
    json_obj = json.loads(json_obj_str)

    file_name = json_obj["file_name"]
    file_size = json_obj["file_size"]

    # checks if upload dir exist, if not creates it.
    if not os.path.exists('upload'):
        os.mkdir('upload')

    cwd = os.getcwd()
    file = open(fr"{cwd}\upload\{file_name}", 'wb')

    # second receive message/file length
    msg_len = int(file_size)

    print('Begin Receiving File...')
    byte_count = 0

    with tqdm(total=msg_len, desc="Processing") as pbar:
        while byte_count < msg_len:
            image_chunk = client_socket.recv(BUFSIZE)
            file.write(image_chunk)
            byte_count += len(image_chunk)

            # Update the tqdm progress bar
            pbar.n = byte_count  # Set the progress bar to the current progress
            pbar.refresh()  # Refresh to update the display

    print(f"{file_name.strip()}, {byte_count} bytes uploaded successfully")
    file.close()
    return fr"{cwd}\upload\{file_name}"


def send_all(**kwargs):
    client_socket = kwargs.get('socket')
    file_name = kwargs.get('file_name')

    file = open(file_name, 'rb')
    file_size = str(os.path.getsize(file_name))
    json_obj = {
        "file_name": file_name,
        "file_size": file_size,
    }
    json_str = json.dumps(json_obj)
    client_socket.send(str(len(json_str)).rjust(HEADER_LEN,'0').encode())  # send file size
    client_socket.send(json_str.encode())


    image_data = 0
    """
    file will be send by BUF_SIZE chunks read from file that need to sent 
    """
    print(f'Begin Sending {file_name.strip()} ...')
    file_size = int(file_size)
    with tqdm(total=file_size, desc="Processing") as pbar:
        while image_data < file_size:
            rxd = file.read(BUFSIZE)
            image_data += len(rxd)
            client_socket.send(rxd)
            # Update the tqdm progress bar
            pbar.n = image_data  # Set the progress bar to the current progress
            pbar.refresh()  # Refresh to update the display

    print(f'{file_name.strip()},  {file_size} bytes Sent Successfully...')
    file.close()
