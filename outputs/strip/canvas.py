from outputs.strip.buffer import Buffer
from outputs.strip.effects.effect import Effect
from outputs.strip.renderer.renderer import Renderer


class Canvas:
    __effects: list[Effect] = []

    def __init__(self, pixels: int, renderer: Renderer):
        self.pixels = pixels
        self.buffer = Buffer(pixels)
        self.__renderer = renderer

    def add_layer(self, effect: Effect):
        self.__effects.append(effect)

    def paint(self):
        # Clear canvas
        self.clear()
        # Run effects
        for effect in self.__effects:
            self.buffer.add(effect.step(Buffer(self.pixels), self.buffer))
        self.__renderer.render(self.buffer)

    def pixel(self, i: int, red: int, green: int, blue: int):
        if i < self.pixels:
            self.buffer.set(i, (red, green, blue))

    def fill(self, red: int, green: int, blue: int):
        for i in range(self.pixels):
            self.buffer.set(i, (red, green, blue))

    def clear(self):
        self.buffer.clear()
