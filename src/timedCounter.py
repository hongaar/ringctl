import threading

from timer import Timer
from counter import Counter


class TimedCounter(Timer):
    def __init__(self, interval: float = 1, n: float = 1):
        self.__counter = Counter()
        super().__init__(self.__counter.increment, interval, n)
    