from inputs.input import Input
from inputs.midiPort import MidiPort


class MidiRange(Input):
    def __init__(self, port: MidiPort, channel: int, initial: int = 0, vmin: int = 0, vmax: int = 127):
        super().__init__(initial=initial, vmin=vmin, vmax=vmax)
        port.listen(channel, self.set)
