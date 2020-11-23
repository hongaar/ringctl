from utils.number import Number


class Middleware:
    pipes: list[tuple[Number, Number]] = []

    def pipe(self, left: Number, right: Number):
        self.pipes.append((left, right))

    def run(self):
        for left, right in self.pipes:
            value = left.get()
            right.set(value)
