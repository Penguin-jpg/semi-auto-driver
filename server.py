import socket
import threading

HEADER = 10
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"


def make_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    return server


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()


def send(server, message):
    message = message.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    server.send(send_length)
    server.send(message)
    print(server.recv(2048).decode(FORMAT))


def start(server):
    print("[STARTING] server is starting...")
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
