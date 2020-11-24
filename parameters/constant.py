from parameters.parameter import Parameter


class Constant(Parameter):
    __value = None

    def __init__(self, value):
        super().__init__()
        self.__value = value

    def set(self, value):
        raise Exception("Constant is immutable")

    def get(self):
        return self.__value
