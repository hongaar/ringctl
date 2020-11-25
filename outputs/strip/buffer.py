from __future__ import annotations


class Buffer:
    def __init__(self, length: int):
        self.length = length
        self.data = self.init_data()

    def init_data(self):
        return [(0, 0, 0)] * self.length

    def set_data(self, data: list[tuple[int, int, int]]):
        self.data = data

    def copy(self):
        copy = Buffer(self.length)
        copy.set_data(self.data.copy())
        return copy

    def alpha(self, alpha: float):
        if alpha < 0 or alpha > 1:
            raise TypeError("Alpha must be within 0-1")
        for i in range(self.length):
            self.set(i, (int(self.data[i][0] * alpha),
                         int(self.data[i][1] * alpha),
                         int(self.data[i][2] * alpha)))
        return self

    def shift(self, x: int):
        new_data = self.init_data()
        for i in range(0, self.length):
            pos = i + x
            if 0 <= pos < self.length:
                new_data[pos] = self.data[i]
        self.data = new_data
        return self

    def clear(self):
        for i in range(self.length):
            self.set(i, (0, 0, 0))
        return self

    def get(self, index: int):
        return self.data[index]

    def set(self, index, color: tuple[int, int, int]):
        self.data[index] = color
        return self

    def add(self, buffer: Buffer):
        new_data = self.init_data()
        for i in range(0, self.length):
            new_data[i] = (min(self.data[i][0] + buffer.get(i)[0], 255),
                           min(self.data[i][1] + buffer.get(i)[1], 255),
                           min(self.data[i][2] + buffer.get(i)[2], 255))
        self.data = new_data
        return self
