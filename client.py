import socket
from simple_socket import make_client, client_send, client_receive

HEADER = 10
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.5"
ADDR = (SERVER, PORT)

def send(client, message):
    message = message.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


client = make_client(SERVER, PORT)
while True:
    try:
        message = client_receive(client)
        if message is not None:
            print(message)
    except KeyboardInterrupt:
        send(DISCONNECT_MESSAGE)
        print("disconnected")
        break
