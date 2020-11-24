from abc import ABC, abstractmethod


class Renderer(ABC):
    @abstractmethod
    def render(self, buffer: list[tuple[int, int, int]]):
        pass
