from outputs.strip.effects.effect import Effect
from parameters.parameter import Parameter


class Shadow(Effect):
    def __init__(self, tail_length: Parameter):
        self.__tail_length = tail_length

    def step(self, canvas, buffer):
        tails = int(self.__tail_length.get())
        for i in range(tails):
            canvas.add(buffer.copy().alpha(1 - (1 / tails * i)).shift(-i))
        return canvas
