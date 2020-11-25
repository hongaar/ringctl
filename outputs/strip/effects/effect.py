from abc import ABC, abstractmethod

from outputs.strip.buffer import Buffer


class Effect(ABC):
    @abstractmethod
    def step(self, canvas: Buffer, buffer: Buffer) -> Buffer:
        pass
