from abc import ABC
from src.Channel import Channel
import base64
from Crypto.Cipher import AES

class ChannelDecorator(Channel, ABC):
    def __init__(self, channel):
        super().__init__()
        self.channel = channel

class StringChannel(ChannelDecorator):
    def __init__(self, channel):
        super().__init__(channel)

    def printLine(self, message):
        try:
            msg = message.encode()
        except AttributeError:
            msg = message
        self.channel.printLine(msg)

    def readLine(self):
        data = self.channel.readLine()
        data = data.decode()
        return data

class BASE64Channel(ChannelDecorator):
    def __init__(self, channel):
        super().__init__(channel)

    def printLine(self, message):
        try:
            msg = base64.b64encode(message.encode())
        except AttributeError:
            msg = base64.b64encode(message)
        self.channel.printLine(msg)

    def readLine(self):
        data = self.channel.readLine()
        try:
            data = base64.b64decode(data.decode())
        except AttributeError:
            data = base64.b64decode(data)
        return data

class AESChannel(ChannelDecorator):
    def __init__(self, channel):
        super().__init__(channel)

        self.key = AES.new('my_key_is_16_byt', AES.MODE_ECB)

    def printLine(self, message):
        try:
            msg = self.key.encrypt(message.encode())
        except AttributeError:
            msg = self.key.encrypt(message)
        self.channel.printLine(msg)

    def readLine(self):
        data = self.channel.readLine()
        try:
            data = self.key.decrypt(data.decode())
        except (AttributeError, UnicodeDecodeError):
            data = self.key.decrypt(data)
        return data