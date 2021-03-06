import threading
import select
import socket

FORMAT = 'utf-8'

class ClientObject():
    
    def __init__(self, conn, addr):
        print(f"[NEW CONNECTION] connected.")
        self.Socket = conn
        self.RemoteAddress = addr

    def getClient(self):
        return self

    def getAddr(self):
        return self.RemoteAddress
    
    def send(self,msg):
        message = msg.encode(FORMAT)
        self.Socket.send(message)