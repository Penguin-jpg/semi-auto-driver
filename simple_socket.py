import socket
import threading

HEADER = 10
FORMAT = "utf-8"

# server
def make_server(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    return server


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        message_length = conn.recv(HEADER).decode(FORMAT)
        if message_length:
            message_length = int(message_length)
            message = conn.recv(message_length).decode(FORMAT)
            if message == "DC":
                connected = False
            print(f"[{addr}] {message}")
            conn.send("Message received".encode(FORMAT))
    conn.close()


def server_start(server):
    print("[STARTING] server is starting...")
    server.listen()
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
    return conn, addr


def server_send(conn, message):
    message = message.encode(FORMAT)
    conn.send(message)
    print(f"'{message}' sent")


# client
def make_client(server_ip, server_port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))
    return client


def client_send(client, message):
    message = message.encode(FORMAT)
    client.send(message)


def client_receive(client):
    message = client.recv(HEADER).decode(FORMAT)
    if message:
        return message
    return None
