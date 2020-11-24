import math

from colr import color

from outputs.strip.renderer.renderer import Renderer


class Terminal(Renderer):
    def __init__(self, columns: int):
        self.columns = columns

    def render(self, buffer: list[tuple[int, int, int]]):
        chars = []
        rows = math.floor(len(buffer) / self.columns)
        for i, item in enumerate(buffer):
            chars.append(color('█', fore=item))
            if (i + 1) % self.columns == 0:
                chars.append('\n')
        # move to beginning of line
        chars.append('\r')
        # move up by number of rows
        chars.append('\033[A' * rows)
        print(''.join(chars), end='')
