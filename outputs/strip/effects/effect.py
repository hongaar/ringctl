from abc import ABC, abstractmethod


class Effect(ABC):
    @abstractmethod
    def step(self, canvas: list[tuple[int, int, int]], buffer: list[tuple[int, int, int]])\
            -> list[tuple[int, int, int]]:
        pass
