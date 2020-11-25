from abc import ABC, abstractmethod

from outputs.strip.buffer import Buffer


class Renderer(ABC):
    @abstractmethod
    def render(self, buffer: Buffer):
        pass
