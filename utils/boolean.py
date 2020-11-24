from utils.variable import Variable


class Boolean(Variable):
    __value = False

    def set(self, value: bool):
        self.__value = value

    def get(self) -> bool:
        return self.__value
