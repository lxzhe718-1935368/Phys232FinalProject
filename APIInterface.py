import time

from queue import Queue
from adafruit_circuitplayground import cp
from time import sleep,monotonic

class Command:
    def __init__(self, comm):
        self.time = comm[0]
        self.type = comm[1]
        self.tone = comm[2]


q = Queue(maxsize  = 100)

while True :
    input_object = Command(input() )# assuming that input is a list with 3 arguments,each is a string
    if input_object.type  == "pennywhistle":
        # Put the command into the queue for later use
        init_time = time.monotonic()
        while time.monotonic()- init_time < input_object.time:
            #to do 
        q.put(input_object)


