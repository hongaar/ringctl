from outputs.strip.effects.effect import Effect
from parameters.color import Color
from parameters.parameter import Parameter


class Chase(Effect):
    __step_counter = 0
    __current_index = 0

    def __init__(self, speed: Parameter, gap: Parameter, color: Color):
        self.__speed = speed
        self.__gap = gap
        self.__color = color

    def step(self, canvas, buffer):
        speed = self.__speed.get()
        gap = int(self.__gap.get())
        if speed > 0:
            steps_per_increment = 1 / self.__speed.get()
            self.__step_counter += 1
            if self.__step_counter >= steps_per_increment:
                self.__step_counter = 0
                self.__current_index += 1
                if self.__current_index >= gap:
                    self.__current_index = 0

        return self.draw(canvas)

    def draw(self, canvas: list[tuple[int, int, int]]):
        gap = int(self.__gap.get())
        pixels = len(canvas)
        for i in range(0, pixels, gap):
            pos = i + self.__current_index
            if pos < pixels:
                canvas[pos] = self.__color.get()
        return canvas
