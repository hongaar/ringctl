from parameters.parameter import Parameter
from utils.any import Any


class Color(Any):
    def __init__(self, red: Parameter, green: Parameter, blue: Parameter, brightness: Parameter):
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__brightness = brightness

    def get(self):
        return (int(self.__red.get() * self.__brightness.get()),
                int(self.__green.get() * self.__brightness.get()),
                int(self.__blue.get() * self.__brightness.get()))
