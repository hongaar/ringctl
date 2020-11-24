from inputs.midiPort import MidiPort
from inputs.toggle import Toggle


class MidiToggle(Toggle):
    def __init__(self, port: MidiPort, channel: int, initial=False):
        super().__init__(initial=initial)
        port.listen(channel, lambda value: self.set(False if value == 0 else True))
