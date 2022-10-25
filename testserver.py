import pickle
import socket
import threading

HEADER = 64
PORT = 5051
SERVER = "v2.wewoo.it"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

with open('loginData.pkl', "rb") as f2:
    login_credentials = pickle.load(f2)


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
            msg = msg.split(" ")
            if msg[0] == "~SIGNUP~":
                if msg[1] not in login_credentials:
                    login_credentials[msg[1]] = msg[2]
                    with open('loginData.pkl', "wb") as f:
                        pickle.dump(login_credentials, f)
                    conn.send("SUCCESSFUL SIGNUP".encode(FORMAT))
                else:
                    conn.send("USERNAME TAKEN".encode(FORMAT))

            elif msg[0] == "~LOGIN~":
                if msg[1] in login_credentials:
                    if msg[2] == login_credentials[msg[1]]:
                        conn.send("LOGIN SUCCESSFUL".encode(FORMAT))
                else:
                    conn.send("INVALID LOGIN".encode(FORMAT))
            else:
                conn.send("NONE".encode(FORMAT))





    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()