import threading
import random
from pprint import pprint
import time
import os

HEIGHT = 50
WIDTH = 30
SLEEP = 0.05
def cls():
    """
    Clears the console
    :return: None
    """
    ## os.system("cls")
    return

class SchneeFlocke(threading.Thread):

    def __init__(self, x, start_event):
        threading.Thread.__init__(self)
        self.event = start_event
        self.x = x
        self.y = 0
        self.closes = False
        self.lock = threading.Lock()

    def run(self):
        self.event.wait()
        # run as long as thread is not closing
        while not self.closes:
            with self.lock:
                time.sleep(SLEEP)
                # Either adds -1, 0 or 1 to the x coordinate
                self.x += round(random.uniform(-1, 1))
                # the x coordinate can't be negative
                # the x coordinate can't be outside of the width
                # Increments the y variable
                self.y += 1
                # checks if the y attribute reached the Floor
                if self.y == HEIGHT:
                    self.closes = True

def visualize(list):
    """
    This method visualizes the List of the threads with the SchneeFlocken
    :param list: List of SchneeFlocken
    :return: None
    """
    matrix = [[0 for x in range(WIDTH)] for y in range(HEIGHT)]

    y = list[0].y
    if y >= HEIGHT:
        y = HEIGHT-1
    for x in range(0, len(matrix[y])):
        for s in list:
            cords = [s.x % WIDTH, s.y]
            if [x, y] == cords:
                print("*", end='')
            else:
                print(" ", end='')
    print()
if __name__ == '__main__':
    start_event = threading.Event()


    s_list = []

    s_count = int(WIDTH/3)
    closed_threads = 0

    # add all Threads to SchneeFlocken-List
    for i in range(0,s_count):
        s_list.append(SchneeFlocke(i*3, start_event))

    for s in s_list:
        s.start()

    # wait a sec
    time.sleep(1)
    # start all Threads with event.set
    start_event.set()

    # run programm as long as there are less closed threads than threads which were started
    while closed_threads < s_count:
        # print out the current list
        # check if a Thread has been closed
        visualize(s_list)
        for s in s_list:
            if s.closes:
                s_list.remove(s)
                closed_threads += 1
        time.sleep(SLEEP)
