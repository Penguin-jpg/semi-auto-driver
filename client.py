import socket

HEADER = 10
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.106"
ADDR = (SERVER, PORT)


def make_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client


def send(client, message):
    message = message.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


while True:
    try:
        message = input()
        send(message)
    except KeyboardInterrupt:
        send(DISCONNECT_MESSAGE)
        print("disconnected")
        break
