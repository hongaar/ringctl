from outputs.strip.effects.effect import Effect
from outputs.strip.renderer.renderer import Renderer


class Canvas:
    __effects: list[Effect] = []

    def __init__(self, pixels: int, renderer: Renderer):
        self.pixels = pixels
        self.buffer = self.empty_buffer()
        self.__renderer = renderer

    def empty_buffer(self):
        return [(0, 0, 0)] * self.pixels

    def add_layer(self, effect: Effect):
        self.__effects.append(effect)

    def paint(self):
        # Clear canvas
        self.clear()
        # Run effects
        for effect in self.__effects:
            self.buffer = self.add_buffer(effect.step(self.empty_buffer(), self.buffer))
        self.__renderer.render(self.buffer)

    def add_buffer(self, buffer: list[tuple[int, int, int]]):
        new_buffer = self.empty_buffer()
        for i, color in enumerate(buffer):
            new_buffer[i] = (min(self.buffer[i][0] + color[0], 255),
                             min(self.buffer[i][1] + color[1], 255),
                             min(self.buffer[i][2] + color[2], 255))
        return new_buffer

    def pixel(self, i: int, red: int, green: int, blue: int):
        if i < self.pixels:
            self.buffer[i] = (red, green, blue)

    def fill(self, red: int, green: int, blue: int):
        for i in range(self.pixels):
            self.pixel(i, red, green, blue)

    def clear(self):
        for i in range(self.pixels):
            self.pixel(i, 0, 0, 0)
