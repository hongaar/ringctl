#!/usr/bin/python

import signal
import sys
import time
from strip import Strip



# SIGINT handler
################################################################################
def signal_handler(signal, frame):
    global app

    app.shutdown()
    sys.exit(0)


# App
################################################################################
class App:
    TICK_SEC = 1


    def __init__(self):
        self.strip = Strip()


    def run(self):
        while True:
            self.strip.color("red")
            print("tick")
            time.sleep(self.TICK_SEC)


    def shutdown(self):
        print("Bye")


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)

    # Run app
    ############################################################################
    app = App()
    app.run()