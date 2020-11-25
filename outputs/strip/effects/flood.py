from outputs.strip.effects.effect import Effect
from parameters.color import Color


class Flood(Effect):
    def __init__(self, color: Color):
        self.__color = color

    def step(self, canvas, buffer):
        pixels = canvas.length
        for i in range(pixels):
            canvas.set(i, self.__color.get())
        return canvas
