from abc import ABC
from src.Channel import Channel
import base64
from Crypto.Cipher import AES

class ChannelDecorator(Channel, ABC):
    # the channel decorator
    def __init__(self, channel):
        """
        Call super constructor of Channel
        :param channel: the channel which gets decaorated
        """
        super().__init__()
        self.channel = channel

class StringChannel(ChannelDecorator):
    # the basic channel, which encrypts and decrypts the string to a byte array
    def __init__(self, channel):
        """
        Call super constructor
        :param channel: the channel which gets decorated
        """
        super().__init__(channel)

    def printLine(self, message):
        """
        implement printLine method, encode the message the message which is to be sent
        :param message: the message which gets sent
        :return: None
        """
        # this try-except is necessary because of complications if the message was already encoded by some other decorator
        try:
            message = message.encode()
        except AttributeError:
            pass
        # call the printLine method of the channel which gets decorated with the encoded message
        self.channel.printLine(message)

    def readLine(self):
        """
        implement readLine method, decode message which got received by the channel which is to be decorated
        :return: the decoded message
        """
        # receive the message from the channel which is to be decorated
        data = self.channel.readLine()
        # this try-except is necessary because of complications if the message was already decoded by some other decorator
        try:
            data = data.encode()
        except AttributeError:
            pass
        return data

class BASE64Channel(ChannelDecorator):
    # decrypt and encrypt string into a BASE64, format
    def __init__(self, channel):
        super().__init__(channel)

    def printLine(self, message):
        """
        implement printLine method with base64 encoding
        :param message: the message which is to be encoded
        :return: None
        """
        try:
            msg = base64.b64encode(message.encode())
        except AttributeError:
            msg = base64.b64encode(message)
        self.channel.printLine(msg)

    def readLine(self):
        """
        implement readLine method with base64 decoding
        :return: the bsae64 decoded string trimmed of its whitespaces
        """
        data = self.channel.readLine()
        try:
            data = base64.b64decode(data.decode())
        except AttributeError:
            data = base64.b64decode(data)
        # the trimming is necessary because the string has to be padded by the AES encoding
        return data.strip()

class AESChannel(ChannelDecorator):
    def __init__(self, channel):
        super().__init__(channel)

        # initialize a key for AES decrypting and encrypting
        # the key has to be exactly 16 chars long
        self.key = AES.new('my_key_is_16_byt', AES.MODE_ECB)

    def printLine(self, message):
        """
        implement the printLine method with AES encryption
        :param message: the message which is to be encrypted
        :return: None
        """
        # the string has to be padded to in order for the AES encryption to work
        message = str(message).rjust(32, ' ')
        try:
            msg = self.key.encrypt(message.encode())
        except AttributeError:
            print(len(message))
            msg = self.key.encrypt(message)
        self.channel.printLine(msg)

    def readLine(self):
        """
        implement the readLine method with AES decryption
        :return: the AES decrypted string trimmed of its whitespaces
        """
        data = self.channel.readLine()
        try:
            data = self.key.decrypt(data.decode())
        except (AttributeError, UnicodeDecodeError):
            data = self.key.decrypt(data)
        # the trimming is necessary because the string has to be padded by the AES encoding
        return data.strip()