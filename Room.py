 
memberDict = {}

class RoomObject:

    def __init__(self, name):
        self.roomname = name

    def client_join(self,client):
        print(f"[NEW CLIENT JOIN THE ROOM] {client.RemoteAddress} join the room...")
        memberDict.update({client.RemoteAddress:client})

    def client_broadcast(self,client,msg):
        for k in memberDict:
            #if k != client.RemoteAddress:
            tmp = memberDict[k]
            tmp.send(msg)