import socket

from Client import *
from RoomAPI import *

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)

clientDict = {}

room_api = RoomAPIObject()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
        print(f"[CLIENT THREAD IS RUNNING] Starting client thread...")
        connected = True
        while connected:
            msg = conn.recv(2046).decode(FORMAT)
            print(f"[{addr}] {msg}")

            if "/roomlist" in msg:
                keys = room_api.get_roomlist()
                print(keys)
            elif "/createroom" in msg:
                tmp = msg.split(" ")
                room_api.create_room(tmp[1])
            elif "/joinroom" in msg:
                client = clientDict.get(addr)
                tmp = msg.split(" ")
                room_api.join_room(client,tmp[1])
            else:
                client = clientDict.get(addr)
                room_api.broadcast_message(client,msg)

        conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        tmp = ClientObject(conn,addr)
        clientDict.update({addr:tmp})
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {len(clientDict)} Client")

print("[SERVER IS STARTING] Starting server ...")
start()