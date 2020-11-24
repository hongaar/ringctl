#!/usr/bin/python
import os
import signal
import sys
import time

from inputs.midiPort import MidiPort
from inputs.midiRange import MidiRange
from inputs.midiToggle import MidiToggle
from inputs.sine import Sine
from inputs.sineClock import SineClock
from middleware.middleware import Middleware
from outputs.strip.canvas import Canvas
from outputs.strip.effects.chase import Chase
from outputs.strip.effects.flood import Flood
from outputs.strip.renderer.terminal import Terminal
from parameters.color import Color
from parameters.parameter import Parameter

# SIGINT handler
################################################################################
from parameters.constant import Constant


def signal_handler(sign, frame):
    global app

    app.shutdown()
    sys.exit(0)


# App
################################################################################
class App:
    def __init__(self, fps: int):
        self.fps = fps

        # Dimensions
        terminal_size = os.get_terminal_size()
        default_lines = terminal_size.lines - 1
        default_columns = terminal_size.columns
        lines = int(input("Lines (" + str(default_lines) + "): ") or default_lines)
        columns = int(input("Columns (" + str(default_columns) + "): ") or default_columns)

        # Parameters
        chase_speed = Parameter(vmax=1)
        chase_gap = Parameter(vmin=3, vmax=100)
        red = Parameter(vmin=0, vmax=255)
        green = Parameter(vmin=0, vmax=255)
        blue = Parameter(vmin=0, vmax=255)
        brightness = Parameter(vmin=0, vmax=1)
        color = Color(red=red, green=green, blue=blue, brightness=brightness)
        pulse_period = Parameter(vmin=0.01, vmax=10, invert=True)

        # Inputs
        midi_port = MidiPort()
        slider1 = MidiRange(port=midi_port, initial=63, channel=0)
        slider2 = MidiRange(port=midi_port, initial=63, channel=1)
        slider3 = MidiRange(port=midi_port, initial=63, channel=2)
        slider4 = MidiRange(port=midi_port, initial=63, channel=3)
        slider5 = MidiRange(port=midi_port, initial=63, channel=4)
        slider6 = MidiRange(port=midi_port, initial=63, channel=5)
        pulse_enabled = MidiToggle(port=midi_port, initial=False, channel=37)
        pulse = SineClock(sine=Sine(period=pulse_period))

        # Middleware
        self.middleware = Middleware()
        self.middleware.pipe(slider1, chase_speed)
        self.middleware.pipe(slider2, chase_gap)
        self.middleware.pipe(slider3, red)
        self.middleware.pipe(slider4, green)
        self.middleware.pipe(slider5, blue)
        self.middleware.pipe_if_true(pulse_enabled, slider6, pulse_period)
        self.middleware.pipe_if_true(pulse_enabled, pulse, brightness)
        self.middleware.pipe_if_false(pulse_enabled, slider6, brightness)

        # Output
        self.canvas = Canvas(pixels=lines * columns, renderer=Terminal(columns=columns))

        chase = Chase(speed=chase_speed, gap=chase_gap, color=color)
        flood = Flood(color=Color(red=Constant(127), green=Constant(127), blue=Constant(255),
                                  brightness=brightness))

        self.canvas.add_layer(chase)
        self.canvas.add_layer(flood)

    def run(self):
        while True:
            self.middleware.run()
            self.canvas.paint()

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
