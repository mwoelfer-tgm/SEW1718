from src.Channel import *
from src.ChannelDecorator import *

if __name__ == '__main__':
    cc = ClientChannel()


    cc = AESChannel(cc)

    cc.printLine("1234567890123456")

    print("Received from Server on Client: " + str(cc.readLine()))

