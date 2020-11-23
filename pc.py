#!/usr/bin/python

import signal
import sys
import time

from inputs.midi import Midi
from middleware.middleware import Middleware
from outputs.strip.effects.chase import Chase
from outputs.strip.renderer.terminal import Terminal
from outputs.strip.strip import Strip
from parameters.parameter import Parameter

# SIGINT handler
################################################################################
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
        slider1 = Midi(channel=0)
        slider2 = Midi(channel=1)
        slider3 = Midi(channel=2)
        slider4 = Midi(channel=3)
        slider5 = Midi(channel=4)

        # Parameters
        speed = Parameter(vmax=1)
        gap = Parameter(vmin=2, vmax=10)
        red = Parameter(vmin=0, vmax=255)
        green = Parameter(vmin=0, vmax=255)
        blue = Parameter(vmin=0, vmax=255)

        # Middleware
        self.middleware = Middleware()
        self.middleware.pipe(slider1, speed)
        self.middleware.pipe(slider2, gap)
        self.middleware.pipe(slider3, red)
        self.middleware.pipe(slider4, green)
        self.middleware.pipe(slider5, blue)

        # Output
        self.strip = Strip(pixels=80, renderer=Terminal(columns=80))
        self.chase = Chase(strip=self.strip, speed=speed, gap=gap, red=red, green=green, blue=blue)

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
