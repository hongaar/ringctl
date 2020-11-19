import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

from store import Store


class SPI(Store):
    __SPI = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
    __CS = digitalio.DigitalInOut(board.D5)

    __mcp = None
    __channel = None

    def __init__(self, pin: int = 0, in_min: float = 0, in_max: float = 3.3, **kwargs):
        super().__init__(in_min, in_max, **kwargs)
        self.__mcp = MCP.MCP3008(self.__SPI, self.__CS)
        self.__channel = AnalogIn(self.__mcp, pin)


    def set(self):
        raise NotImplementedError


    def get(self):
        return self.normalize_in(self.__channel.voltage)
