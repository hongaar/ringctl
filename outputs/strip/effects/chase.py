from outputs.strip.strip import Strip
from parameters.parameter import Parameter


class Chase:
    __tick_counter = 0
    __current_index = 0

    def __init__(self, strip: Strip, speed: Parameter, gap: Parameter, red: Parameter,
                 green: Parameter, blue: Parameter):
        self.__strip = strip
        self.__speed = speed
        self.__gap = gap
        self.__red = red
        self.__green = green
        self.__blue = blue

    def tick(self):
        speed = self.__speed.get()
        if speed == 0:
            return
        ticks_per_step = 1 / self.__speed.get()
        self.__tick_counter += 1
        if self.__tick_counter >= ticks_per_step:
            self.__tick_counter = 0
            self.step()

    def step(self):
        gap = int(self.__gap.get())
        for i in range(0, self.__strip.pixels, gap):
            self.__strip.pixel(i + self.__current_index, int(self.__red.get()),
                               int(self.__green.get()), int(self.__blue.get()))
        self.__strip.render()
        for i in range(0, self.__strip.pixels, gap):
            self.__strip.pixel(i + self.__current_index, 0, 0, 0)
        self.__current_index += 1
        if self.__current_index >= gap:
            self.__current_index = 0
