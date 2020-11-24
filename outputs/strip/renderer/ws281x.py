from rpi_ws281x import Adafruit_NeoPixel, Color

from outputs.strip.renderer.renderer import Renderer


class Ws281x(Renderer):
    __LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
    __LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
    __LED_DMA = 10  # DMA channel to use for generating signal (try 10)
    __LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
    __LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
    __LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53

    def __init__(self, led_count: int):
        self.led_count = led_count
        self.__strip = Adafruit_NeoPixel(
            self.led_count,
            self.__LED_PIN,
            self.__LED_FREQ_HZ,
            self.__LED_DMA,
            self.__LED_INVERT,
            self.__LED_BRIGHTNESS,
            self.__LED_CHANNEL
        )
        self.__strip.begin()

    def render(self, buffer: list[tuple[int, int, int]]):
        for i, color in enumerate(buffer):
            self.__strip.setPixelColor(i, Color(*color))
        self.__strip.show()
