#!/usr/bin/python
import os
import signal
import sys
import time

from inputs.midiRange import MidiRange
from inputs.sine import Sine
from inputs.sineClock import SineClock
from inputs.timeElapsed import TimeElapsed
from middleware.middleware import Middleware
from outputs.strip.effects.chase import Chase
from outputs.strip.renderer.terminal import Terminal
from outputs.strip.strip import Strip
from parameters.color import Color
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
    def __init__(self, fps: int):
        self.fps = fps

        # Get terminal dimensions
        size = os.get_terminal_size()

        # Get second counter
        elapsed = TimeElapsed()

        # Parameters
        chase_speed = Parameter(vmax=1)
        chase_gap = Parameter(vmin=2, vmax=10)
        red = Parameter(vmin=0, vmax=255)
        green = Parameter(vmin=0, vmax=255)
        blue = Parameter(vmin=0, vmax=255)
        brightness = Parameter(vmin=0, vmax=1)
        color = Color(red=red, green=green, blue=blue, brightness=brightness)
        pulse_period = Parameter(vmin=0.01, vmax=10)

        # Inputs
        slider1 = MidiRange(initial=63, channel=0)
        slider2 = MidiRange(initial=63, channel=1)
        slider3 = MidiRange(initial=63, channel=2)
        slider4 = MidiRange(initial=63, channel=3)
        slider5 = MidiRange(initial=63, channel=4)
        slider6 = MidiRange(initial=63, channel=5)
        pulse_enabled = MidiRange(initial=63, channel=37)
        pulse = SineClock(sine=Sine(period=pulse_period))

        # Middleware
        self.middleware = Middleware()
        self.middleware.pipe(slider1, chase_speed)
        self.middleware.pipe(slider2, chase_gap)
        self.middleware.pipe(slider3, red)
        self.middleware.pipe(slider4, green)
        self.middleware.pipe(slider5, blue)
        self.middleware.pipe(slider6, pulse_period)
        self.middleware.pipe(pulse, brightness)

        # Output
        self.strip = Strip(pixels=size.columns * (size.lines - 1),
                           renderer=Terminal(columns=size.columns))
        self.chase = Chase(strip=self.strip, speed=chase_speed, gap=chase_gap, color=color)

    def run(self):
        while True:
            self.middleware.run()
            self.chase.tick()

            # Pause for a bit depending on app fps
            time.sleep(1 / self.fps)

    def shutdown(self):
        os.system('clear')
        print("bye")


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)

    # Run app
    ############################################################################
    app = App(fps=120)
    app.run()
