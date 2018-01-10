from src.Channel import *
from src.ChannelDecorator import *

if __name__ == '__main__':
    # initialize a CientChannel and decorate it with a StringChannel so a string can be sent and received
    cc = StringChannel(ClientChannel())

    # decorate with BASE64 channel
    cc = BASE64Channel(cc)
    # decorate further with AES channel
    cc = AESChannel(cc)

    # print a message to the server, which is 16 chars long for AES encryption
    cc.printLine("1234567890123456")

    # receive a message from the server
    print("Received from Server on Client: " + str(cc.readLine()))

