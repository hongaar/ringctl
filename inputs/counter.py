from utils.number import Number


class Counter(Number):
    def __init__(self, step: float = 1):
        self.__step = step

    def increment(self):
        self.set(self.get() + self.__step)
        return self.get()

    def decrement(self):
        self.set(self.get() - self.__step)
        return self.get()
