from greyscale_algorithm import GreyscaleAlgorithm
import copy


class GreyscaleByAverage(GreyscaleAlgorithm):

    averagedPixels = []
    def __init__(self, image, pixelList):
        GreyscaleAlgorithm.__init__(self, image, pixelList)

    def grey_pixels(self):
        averagedPixels = []
        for pixel in self.pixelList:
            average = round((pixel.get_red() + pixel.get_green() + pixel.get_blue()) / 3)
            averagedpixel = copy.copy(pixel)
            averagedpixel.set_red(average)
            averagedpixel.set_green(average)
            averagedpixel.set_blue(average)
            averagedPixels.append(averagedpixel)
        self.averagedPixels = averagedPixels

    def get_pixellist(self):
        return super(GreyscaleByAverage, self).get_pixellist()

    def get_averagedPixels(self):
        return self.averagedPixels

    def grey_image(self):
        return super(GreyscaleByAverage, self).grey_image(self.averagedPixels)