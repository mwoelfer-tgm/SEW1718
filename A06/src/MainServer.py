from src.Channel import *
from src.ChannelDecorator import *

if __name__ == '__main__':

    sc = ServerChannel()

    sc = AESChannel(sc)



    print("Received from Client on the Server: " + str(sc.readLine()))

    sc.printLine("1234567890123456")

