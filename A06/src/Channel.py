from abc import ABC, abstractmethod
import socket

class Channel(ABC):
    # the main component
    def __init__(self):
        """
        """
        self.socket = socket.socket()

    @abstractmethod
    def printLine(self, message):
        pass

    @abstractmethod
    def readLine(self):
        pass

class ClientChannel(Channel):
    def __init__(self):
        super().__init__()
        self.socket.connect(('localhost', 50000))


    def printLine(self, message):
        self.socket.send(message)

    def readLine(self):
        data = self.socket.recv(1024)
        if not data:
            self.socket.close()
        else:
            return data

class ServerChannel(Channel):
    def __init__(self):

        super().__init__()

        self.socket.bind(('localhost', 50000))
        self.socket.listen(5)

        (self.clientsocket, self.address) = self.socket.accept()
        print("A Client has successfully connected to the server!")

    def readLine(self):
        data = self.clientsocket.recv(1024)
        if not data:
            self.clientsocket.close()
        else:
            return data

    def printLine(self, message):
        self.clientsocket.send(message)