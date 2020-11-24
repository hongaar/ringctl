from typing import Callable

from utils.boolean import Boolean
from utils.variable import Variable


class Middleware:
    pipes: list[tuple[Variable, Variable, Callable[[], bool]]] = []

    def pipe(self, left: Variable, right: Variable):
        self.pipes.append((left, right, lambda: True))

    def pipe_if_true(self, condition: Boolean, left: Variable, right: Variable):
        self.pipes.append((left, right, lambda: condition.get()))

    def pipe_if_false(self, condition: Boolean, left: Variable, right: Variable):
        self.pipes.append((left, right, lambda: not condition.get()))

    def run(self):
        for left, right, condition in self.pipes:
            if condition():
                value = left.get()
                right.set(value)
