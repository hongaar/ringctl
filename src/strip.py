from rpi_ws281x import *


class Strip:
    # LED strip configuration:
    LED_COUNT      = 150      # Number of LED pixels.
    LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
    LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
    LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
    LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
    LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

    # Define colors which will be used by the example.  Each color is an unsigned
    # 32-bit value where the lower 24 bits define the red, green, blue data (each
    # being 8 bits long).
    DOT_COLORS = {
        'red':      [255, 0, 0],
        'green':    [0, 255, 0],
        'blue':     [0, 0, 255],

        'white':    [255, 255, 255],

        'yellow':   [255, 255, 0],
        'pink':     [255, 0, 255],
        'cyan':     [0, 255, 255]
    }

    def __init__(self):
        self.__strip = Adafruit_NeoPixel(
            self.LED_COUNT,
            self.LED_PIN,
            self.LED_FREQ_HZ,
            self.LED_DMA,
            self.LED_INVERT,
            self.LED_BRIGHTNESS,
            self.LED_CHANNEL
        )
        self.__strip.begin()


    def __set_color(self, color):
        for i in range(self.__strip.numPixels()):
            self.__strip.setPixelColor(i, color)
        self.__strip.show()


    def rgb(self, red, green, blue):
        self.__set_color(Color(red, green, blue))


    def color(self, color):
        try:
            color = self.DOT_COLORS[color]
            self.rgb(color[0], color[1], color[2])
        except KeyError:
            print("Color " + color + " not found")