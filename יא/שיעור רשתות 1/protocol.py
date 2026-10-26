BUFSIZE = 3
HEADER_LEN = 4

def recv_all(**kwargs):
    client_socket = kwargs.get('socket')
    recv_data = b''
    msg_len = client_socket.recv(HEADER_LEN).decode()
    if msg_len == '':
        return ''
    msg_len = int(msg_len)

    while len(recv_data) < msg_len:
        recv_data += client_socket.recv(BUFSIZE)

    print(f"recieved {recv_data.decode()}")
    return recv_data.decode()

def send_all(**kwargs):
    data = kwargs.get('data',"ERROR No Data Received")
    client_socket = kwargs.get('socket')
    msg_len = str(len(data)).rjust(HEADER_LEN,'0')
    send_msg = msg_len +data
    client_socket.send(send_msg.encode())
    print(f"sent {send_msg}")