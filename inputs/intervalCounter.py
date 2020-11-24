from inputs.counter import Counter
from inputs.timer import Timer


class IntervalCounter(Timer):
    def __init__(self, counter: Counter, interval: float = 1):
        super().__init__(interval=interval, fn=counter.increment)
