from rpi_ws281x import Adafruit_NeoPixel, Color


class Strip:
    # LED strip configuration:
    __LED_PIN = 18 # GPIO pin connected to the pixels (18 uses PWM!).
    __LED_FREQ_HZ = 800000 # LED signal frequency in hertz (usually 800khz)
    __LED_DMA = 10 # DMA channel to use for generating signal (try 10)
    __LED_BRIGHTNESS = 255 # Set to 0 for darkest and 255 for brightest
    __LED_INVERT = False # True to invert the signal (when using NPN transistor level shift)
    __LED_CHANNEL = 0 # set to '1' for GPIOs 13, 19, 41, 45 or 53

    pixel_count: int = None # Number of LED pixels.

    def __init__(self, pixel_count: int):
        self.pixel_count = pixel_count
        self.__strip = Adafruit_NeoPixel(
            self.pixel_count,
            self.__LED_PIN,
            self.__LED_FREQ_HZ,
            self.__LED_DMA,
            self.__LED_INVERT,
            self.__LED_BRIGHTNESS,
            self.__LED_CHANNEL
        )
        self.__strip.begin()


    def __set_color(self, i: int, color: Color):
        self.__strip.setPixelColor(i, color)


    def render(self):
        self.__strip.show()


    def pixel(self, i: int, red: int, green: int, blue: int):
        self.__strip.setPixelColor(i, Color(red, green, blue))


    def fill(self, red: int, green: int, blue: int):
        for i in range(self.__strip.numPixels()):
            self.pixel(i, red, green, blue)


    def off(self):
        for i in range(self.__strip.numPixels()):
            self.pixel(i, 0, 0, 0)
