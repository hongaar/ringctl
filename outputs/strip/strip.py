from outputs.strip.renderer.renderer import Renderer


class Strip:
    def __init__(self, pixels: int, renderer: Renderer):
        self.pixels = pixels
        self.buffer = [(0, 0, 0)] * pixels
        self.__renderer = renderer

    def render(self):
        self.__renderer.render(self.buffer)

    def pixel(self, i: int, red: int, green: int, blue: int):
        if i < self.pixels:
            self.buffer[i] = (red, green, blue)

    def fill(self, red: int, green: int, blue: int):
        for i in range(self.pixels):
            self.pixel(i, red, green, blue)

    def off(self):
        for i in range(self.pixels):
            self.pixel(i, 0, 0, 0)
