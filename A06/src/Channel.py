from abc import ABC, abstractmethod
import socket

class Channel(ABC):
    # the main component
    def __init__(self):
        """
        Initialize a socket object
        """
        self.socket = socket.socket()

    @abstractmethod
    def printLine(self, message):
        """
        Define abstract printLine method
        :param message: The message to be printed
        :return: None
        """
        pass

    @abstractmethod
    def readLine(self):
        """
        Define abstract readLine method
        :return: None
        """
        pass

class ClientChannel(Channel):
    def __init__(self):
        """
        Connect the client channel to the server
        """
        super().__init__()
        self.socket.connect(('localhost', 50000))


    def printLine(self, message):
        """
        Implement printLine method, sends message to server
        :param message: Message to be sent to server
        :return: None
        """
        self.socket.send(message)

    def readLine(self):
        """
        Implement readLine method, receive response from server
        :return: the data received from the server
        """
        data = self.socket.recv(1024)
        if not data:
            self.socket.close()
        else:
            return data

class ServerChannel(Channel):
    def __init__(self):
        """
        Bind the server channel for a client channel to connect
        """
        super().__init__()

        self.socket.bind(('localhost', 50000))
        self.socket.listen(5)

        (self.clientsocket, self.address) = self.socket.accept()
        print("A Client has successfully connected to the server!")

    def readLine(self):
        """
        Implement readLine method, receive data from client channel
        :return: the data received from client
        """
        data = self.clientsocket.recv(1024)
        if not data:
            self.clientsocket.close()
        else:
            return data.strip()

    def printLine(self, message):
        """
        Implement the printLine method, send response to the client
        :param message: the message to be sent to the client
        :return: None
        """
        self.clientsocket.send(message)