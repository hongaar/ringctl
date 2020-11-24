from outputs.strip.effects.effect import Effect
from parameters.color import Color


class Flood(Effect):
    def __init__(self, color: Color):
        self.__color = color

    def step(self, canvas, buffer):
        pixels = len(canvas)
        for i in range(0, pixels):
            canvas[i] = self.__color.get()
        return canvas
