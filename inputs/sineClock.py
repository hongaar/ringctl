import math

from inputs.sine import Sine
from inputs.timeElapsed import TimeElapsed
from utils.number import Number


class SineClock(Number):
    def __init__(self, sine: Sine):
        self.__sine = sine
        self.__elapsed = TimeElapsed()

    def get(self):
        return self.__sine.at_time(self.__elapsed.get())

