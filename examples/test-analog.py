import time
from rpi_ws281x import *
import busio
import digitalio
import board
import time
import numpy
from easing_functions import *
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


# LED strip configuration:
LED_COUNT      = 150      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# sound sensor
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)
mcp = MCP.MCP3008(spi, cs)

channel = AnalogIn(mcp, MCP.P0)

interval = 0.01
moving_average = 0.05 # seconds
max_voltage = 2.2
slots = int((1 / interval) * moving_average)
measurements = [0] * slots
index = 0
min_value = -65
max_value = 127
threshold = 100
use_average = True


def set_color(strip, color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()


# Main program logic follows:
if __name__ == '__main__':
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

    ease = QuadEaseIn(start=min_value, end=max_value, duration=max_voltage)

    while True:
        if use_average:
            index += 1
            if index > slots - 1:
                index = 0
            measurements[index] = channel.voltage
            voltage = numpy.mean(measurements)
        else:
            voltage = channel.voltage
        
        value = int(ease.ease(voltage))
        value = max(value, 0)
        value = min(value, max_value)
        
        print(str(value) + '                       ', end='\r')
        set_color(strip, Color(value, int(0.1*value), 0))
        time.sleep(interval)

