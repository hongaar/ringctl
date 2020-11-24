import math

from parameters.parameter import Parameter
from utils.number import Number


class Sine(Number):
    def __init__(self, period: Parameter):
        self.__period = period
        self.__vmin = 0
        self.__vmax = 1

    # noinspection PyPep8Naming
    def at_time(self, t: float):
        # y = A ⋅ sin(B(x + C)) + D
        # Where,
        # Amplitude = A
        # Period = 2pi / B
        # Horizontal Shift = C
        # Vertical Shift = D
        A = (self.__vmax - self.__vmin) / 2
        B = (2 * math.pi) / self.__period.get()
        C = self.__period.get() * 0.75
        D = (self.__vmax - self.__vmin) / 2
        y = A * math.sin(B * (t + C)) + D
        self.set(y)
        return self.get()

