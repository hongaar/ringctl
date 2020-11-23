from colr import color

from outputs.strip.renderer.renderer import Renderer


class Terminal(Renderer):
    def __init__(self, columns: int):
        self.columns = columns

    def render(self, buffer: dict[int, tuple[int, int, int]]):
        chars = []
        for i in range(self.columns):
            chars.append(color('█', fore=buffer[i]))
        print(''.join(chars), end='\r')
