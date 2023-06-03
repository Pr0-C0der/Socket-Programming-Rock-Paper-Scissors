import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.7" #Put your IP Address Here
        self.port = 5559
        self.addr = (self.server, self.port)
        self.p = self.connect()
    def send(self, data):#Sending the data
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048*2))
        except socket.error as e:
            print(e)
            
    def connect(self): #Connecting
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def getP(self):
        return self.p



