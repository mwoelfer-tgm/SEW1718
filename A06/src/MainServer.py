from src.Channel import *
from src.ChannelDecorator import *

if __name__ == '__main__':

    # initialize a ServerChannel and decorate it with a StringChannel so a string can be received and sent
    sc = StringChannel(ServerChannel())

    # decorate with base64 channel
    sc = BASE64Channel(sc)
    # decorate further with AES channel
    sc = AESChannel(sc)

    # print the message which gets received by the server
    print("Received from Client on the Server: " + str(sc.readLine()))

    # print a response to the server, which is 16 chars long for AES encryption
    sc.printLine("1234567890123456")

