import math

from colr import color

from outputs.strip.buffer import Buffer
from outputs.strip.renderer.renderer import Renderer


class Terminal(Renderer):
    def __init__(self, columns: int):
        self.columns = columns

    def render(self, buffer: Buffer):
        chars = []
        length = buffer.length
        rows = math.floor(length / self.columns)
        for i in range(length):
            chars.append(color('█', fore=buffer.get(i)))
            if (i + 1) % self.columns == 0:
                chars.append('\n')
        # move to beginning of line
        chars.append('\r')
        # move up by number of rows
        chars.append('\033[A' * rows)
        print(''.join(chars), end='')
