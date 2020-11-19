import threading

from store import Store


class Timer(Store):
    def __init__(self, fn: callable, interval: float = 1, *args):
        super().__init__()
        self.fn = fn
        self.args = args
        self.interval = interval
        self.__createTimer()
    

    def __createTimer(self):
        self.__timer = threading.Timer(self.interval, self.tick)
        self.__timer.start()


    def __deleteTimer(self):
        if (self.__timer):
            self.__timer._delete()


    def tick(self):
        self.__deleteTimer()
        value = self.fn(*self.args)
        self.set(value)
        self.__createTimer()
