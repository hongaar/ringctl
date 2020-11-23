from outputs.strip.renderer.renderer import Renderer


class Strip:
    buffer: dict[int, tuple[int, int, int]] = {}

    def __init__(self, pixels: int, renderer: Renderer):
        self.pixels = pixels
        self.__renderer = renderer
        # Initialize all pixels to off
        self.off()

    def render(self):
        self.__renderer.render(self.buffer)

    def pixel(self, i: int, red: int, green: int, blue: int):
        self.buffer[i] = (red, green, blue)

    def fill(self, red: int, green: int, blue: int):
        for i in range(self.pixels):
            self.pixel(i, red, green, blue)

    def off(self):
        for i in range(self.pixels):
            self.pixel(i, 0, 0, 0)
