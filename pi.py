#!/usr/bin/python

import signal
import sys
import time

from inputs.spi import SPI
from middleware.middleware import Middleware
from outputs import strip


# SIGINT handler
################################################################################
from outputs.strip.effects.chase import Chase
from parameters.parameter import Parameter


def signal_handler(sign, frame):
    global app

    app.shutdown()
    sys.exit(0)


# App
################################################################################
class App:
    def __init__(self, frequency: int):
        self.frequency = frequency

        # Inputs
        self.knob = SPI(pin=2)
        self.proximity = SPI(pin=0, vmin=1.3, vmax=2.2)

        # Parameters
        self.speed = Parameter(vmax=0.5)
        self.gap = Parameter(vmin=2, vmax=10)

        # Middleware
        self.middleware = Middleware()
        self.middleware.pipe(self.knob, self.proximity)
        self.middleware.pipe(self.proximity, self.speed)

        # Output
        self.strip = strip.Strip(pixels=150)
        self.chase = Chase(strip=self.strip, speed=self.speed, gap=self.gap)

        # self.timedCounter = TimedCounter(interval=0.1, n=1)

    def run(self):
        while True:
            self.middleware.run()

            self.chase.tick()

            # Pause for a bit depending on app frequency
            time.sleep(1 / self.frequency)

    def shutdown(self):
        print("Bye")


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)

    # Run app
    ############################################################################
    app = App(frequency=60)
    app.run()