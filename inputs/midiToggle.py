from rtmidi.midiutil import open_midiinput

from inputs.input import Input


MIDI_IN_PORT = 0
channel_listeners = {}


def midi_handler(event, data=None):
    message, _ = event
    _, channel, value = message
    if channel in channel_listeners:
        channel_listeners[channel](value)


midi_in, port_name = open_midiinput(MIDI_IN_PORT)
midi_in.set_callback(midi_handler)


class MidiRange(Input):
    def __init__(self, channel: int, initial: int = 0, vmin: int = 0, vmax: int = 127):
        super().__init__(initial=initial, vmin=vmin, vmax=vmax)
        channel_listeners[channel] = super().set
