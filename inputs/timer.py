import threading
from typing import Callable

from utils.number import Number


class Timer(Number):
    def __init__(self, interval: float, fn: Callable[..., float], *args):
        self.interval = interval
        self.fn = fn
        self.args = args
        self.__create_timer()

    def __create_timer(self):
        self.__timer = threading.Timer(self.interval, self.tick)
        self.__timer.start()

    def __delete_timer(self):
        if self.__timer:
            self.__timer.cancel()

    def tick(self):
        self.__delete_timer()
        value = self.fn(*self.args)
        self.set(value)
        self.__create_timer()
