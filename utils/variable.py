from abc import ABC, abstractmethod


class Variable(ABC):
    @abstractmethod
    def set(self, value):
        pass

    @abstractmethod
    def get(self):
        pass
