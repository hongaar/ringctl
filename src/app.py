#!/usr/bin/python

import signal
import sys
import time

from strip import Strip
from timedCounter import TimedCounter


# SIGINT handler
################################################################################
def signal_handler(signal, frame):
    global app

    app.shutdown()
    sys.exit(0)


# App
################################################################################
class App:
    def __init__(self, frequency: int):
        self.frequency = frequency
        self.strip = Strip()
        self.timedCounter = TimedCounter(interval=0.1, n=1)


    def run(self):
        while True:
            # self.strip.color("red")
            print("From timedCounter: " + str(self.timedCounter.get()))
            time.sleep(1 / self.frequency)


    def shutdown(self):
        print("Bye")


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)

    # Run app
    ############################################################################
    app = App(frequency=10)
    app.run()