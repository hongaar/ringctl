from abc import ABC, abstractmethod


class Renderer(ABC):
    @abstractmethod
    def render(self, buffer: dict[int, tuple[int, int, int]]):
        pass
