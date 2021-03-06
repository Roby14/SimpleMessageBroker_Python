from Room import *

roomDict = {}
ClientMap = {}

class RoomAPIObject:
    
    def __init__(self):
        print("[INITIALIZE ROOM API] Room API is initialized...")
        
    def get_roomlist(self):
        return roomDict.keys()

    def create_room(self,roomname):
        tmp = RoomObject(roomname)
        roomDict.update({roomname:tmp})
        print(f"[NEW ROOM CREATED] {roomname} created...")

    def join_room(self,client,roomname):
        if roomname in roomDict:
            print("ada")
            tmp = roomDict[roomname]
            tmp.client_join(client)
            ClientMap.update({client.RemoteAddress:tmp})
        else:
            print("gada")

    def broadcast_message(self,client,msg):
        if client.RemoteAddress in ClientMap:
            tmp = ClientMap[client.RemoteAddress]
            tmp.client_broadcast(client,msg)
