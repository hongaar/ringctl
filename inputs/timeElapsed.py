import time

from utils.number import Number


class TimeElapsed(Number):
    def __init__(self):
        self.__start_ms = time.time()

    def get(self):
        return time.time() - self.__start_ms
