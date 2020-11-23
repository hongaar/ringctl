"""
Use an input when you need to normalize the input range (e.g. analog sensor). Call the set() method
with a value in range vmin-vmax. The get() method will return a value in range 0-1.
"""
from utils.number import Number


class Input(Number):
    def __init__(self, vmin: float = 0, vmax: float = 1):
        self.vmin = vmin
        self.vmax = vmax

    def set(self, value: float):
        # Limit value to vmin and vmax
        limited = min(self.vmax, max(self.vmin, value))
        # Normalize to range 0-1
        normalized = (limited - self.vmin) / (self.vmax - self.vmin)
        super().set(normalized)
