BUFSIZE = 2048
FILE_SIZE = 10
FILE_NAME_LEN = 30
import os
from tqdm import tqdm

def recv_all(**kwargs):
    client_socket = kwargs.get('socket')
    # first receive file name
    file_name = str(client_socket.recv(FILE_NAME_LEN).decode()).strip()
    if file_name == '':
        return ''

    # checks if upload dir exist, if not creates it.
    if not os.path.exists('upload'):
        os.mkdir('upload')

    cwd = os.getcwd()
    file = open(fr"{cwd}\upload\{file_name}", 'wb')

    # second receive message/file length
    msg_len = client_socket.recv(FILE_SIZE).decode()
    msg_len = int(msg_len)

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
    file_name = file_name.rjust(FILE_NAME_LEN, ' ')
    client_socket.send(file_name.encode())  # send file name first
    msg_len = str(file_size).rjust(FILE_SIZE, '0').encode()
    client_socket.send(msg_len)  # send file size second

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
