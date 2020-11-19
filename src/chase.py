from strip import Strip
from store import Store


class Chase:
    color = (255, 0, 0)

    __tick_counter = 0
    __current_index = 0

    #__strip: Strip = None

    def __init__(self, strip: Strip, speed: Store, gap: Store):
        self.__strip = strip
        self.__speed = speed
        self.__gap = gap


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
        for i in range(0, self.__strip.pixel_count, gap):
            self.__strip.pixel(i + self.__current_index, *self.color)
        self.__strip.render()
        for i in range(0, self.__strip.pixel_count, gap):
            self.__strip.pixel(i + self.__current_index, 0, 0, 0)
        self.__current_index += 1
        if self.__current_index >= gap:
            self.__current_index = 0
        