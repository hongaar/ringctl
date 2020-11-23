"""
Use a parameter when you need to normalize the output range (e.g. digital signal). Call the set()
method with a value in range 0-1. The get() method will return a value in range vmin-vmax.
"""
from utils.number import Number


class Parameter(Number):
    def __init__(self, vmin: float = 0, vmax: float = 1):
        self.vmin = vmin
        self.vmax = vmax

    def get(self) -> float:
        return super().get() * (self.vmax - self.vmin) + self.vmin
