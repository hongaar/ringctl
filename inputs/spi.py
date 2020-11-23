import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as mcp
from adafruit_mcp3xxx.analog_in import AnalogIn

from inputs.input import Input


class SPI(Input):
    __SPI = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
    __CS = digitalio.DigitalInOut(board.D5)

    __mcp = None
    __channel = None

    def __init__(self, pin: int = 0, vmin: float = 0, vmax: float = 3.3):
        super().__init__(vmin, vmax)
        self.__mcp = mcp.MCP3008(self.__SPI, self.__CS)
        self.__channel = AnalogIn(self.__mcp, pin)

    def get(self):
        super().set(self.__channel.voltage)
        return super().get()
