from utils.variable import Variable


class Number(Variable):
    __value: float = 0

    def set(self, value: float):
        self.__value = value

    def get(self) -> float:
        return self.__value
