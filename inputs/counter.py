from utils.number import Number


class Counter(Number):
    def increment(self, n: float = 1):
        self.set(self.get() + n)
        return self.get()

    def decrement(self, n: float = 1):
        self.set(self.get() - n)
        return self.get()
