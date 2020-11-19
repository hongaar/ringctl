#!/usr/bin/python

import signal
import sys
import time

from strip import Strip
from timedCounter import TimedCounter
from spi import SPI
from store import Store
from chase import Chase


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
        self.strip = Strip(pixel_count=150)
        self.speed = Store(out_max=0.5)
        self.gap = Store(out_min=2, out_max=10)
        self.chase = Chase(strip=self.strip, speed=self.speed, gap=self.gap)
        # self.timedCounter = TimedCounter(interval=0.1, n=1)
        self.potmeter = SPI(pin=2)
        self.proximity = SPI(pin=0, in_min=1.3, in_max=2.2)


    def run(self):
        while True:
            self.speed.set(self.proximity.get())
            self.gap.set(self.potmeter.get())
            # print("proximity: " + str(self.proximity.get()))
            # print("speed: " + str(self.speed.get()))
            # print("potmeter: " + str(self.potmeter.get()))
            # print("gap: " + str(self.gap.get()))

            self.chase.tick()
            time.sleep(1 / self.frequency)


    def shutdown(self):
        print("Bye")


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)

    # Run app
    ############################################################################
    app = App(frequency=60)
    app.run()