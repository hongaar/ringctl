from inputs.counter import Counter
from inputs.timer import Timer


class TimedCounter(Timer):
    def __init__(self, interval: float = 1, n: float = 1):
        self.__counter = Counter()
        super().__init__(self.__counter.increment, interval, n)
