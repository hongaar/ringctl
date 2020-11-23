class Number:
    __value: float = 0

    def set(self, value: float):
        self.__value = value

    def get(self) -> float:
        return self.__value
