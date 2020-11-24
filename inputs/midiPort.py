import os
from typing import Callable

from rtmidi.midiutil import open_midiinput

from utils.number import Number
from utils.variable import Variable

MIDI_IN_PORT = 0
channel_listeners = {}


def midi_handler(event, data=None):
    message, _ = event
    _, channel, value = message
    if channel in channel_listeners:
        channel_listeners[channel](value)


midi_in, port_name = open_midiinput(MIDI_IN_PORT)
midi_in.set_callback(midi_handler)


class MidiPort:
    def __init__(self, port: int = 0):
        if port != 0:
            raise Exception('Port must be 0')
        pass

    def listen(self, channel: int, listener: Callable[[int], None]):
        channel_listeners[channel] = listener
