import threading

from store import Store


class Counter(Store):
    count = 0


    def __init__(self):
        super().__init__()
    

    def increment(self, n: float = 1):
        self.count += n
        self.set(self.count)
        return self.count


    def decrement(self, n: float = 1):
        self.count -= n
        self.set(self.count)
        return self.count
