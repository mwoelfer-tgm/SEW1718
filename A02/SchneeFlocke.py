import threading
import random
import time
import os

counter = 0
HEIGHT = 40
WIDTH = 100

def cls():
    """
    Clears the console
    :return: None
    """
    os.system("cls")

class SchneeFlocke(threading.Thread):
    def __init__(self, x):
        threading.Thread.__init__(self)
        self.x = x
        self.y = 0
        self.closes = False
        self.lock = threading.Lock()

    def run(self):
        # run as long as thread is not closing
        while not self.closes:
            time.sleep(0.3)
            # Either adds -1, 0 or 1 to the x coordinate
            self.x += round(random.uniform(-1, 1))
            # Increments the y variable
            self.y += 1
            # checks if the y attribute reached the Floor
            if self.y == HEIGHT:
                self.closes = True


        self.lock.acquire()
        # release the lock
        self.lock.release()

def visualize(list):
    """
    This method visualizes the List of the threads with the SchneeFlocken
    :param list: List of SchneeFlocken
    :return: None
    """
    # This is supposed to 'buffer' everything to simualte the y height
    for i in range(0, list[0].y):
        print()
    # Iterate through the list
    for i in range(0, len(list)):
        # Print out an icon for each SchneeFlocke
        print("*",end='')
        # Print the x cord as the distance between each SchneeFlocke
        for i in range(0, list[i].x - i):
            print(" ",end='')

if __name__ == '__main__':
    s_list = []

    s_count = int(WIDTH/3)
    closed_threads = 0

    # add all Threads to SchneeFlocken-List
    for i in range(0,s_count):
        s_list.append(SchneeFlocke(i*3))

    # start all Threads
    for s in s_list:
        s.start()

    # clear console
    cls()
    # run programm as long as there are less closed threads than threads which were started
    while closed_threads < s_count:
        # print out the current list
        visualize(s_list)
        # check if a Thread has been closed
        for s in s_list:
            if s.closes:
                s_list.remove(s)
                closed_threads += 1
        time.sleep(0.1)
        # clear console
        cls()
