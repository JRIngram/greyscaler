from abc import ABC, abstractmethod
from PIL import Image


class GreyscaleAlgorithm(ABC):


    def __init__(self, image, pixellist):
        self.pixelList = pixellist
        self.image = image

    @abstractmethod
    def grey_pixels(self):
        pass

    def get_pixellist(self):
        return self.pixelList

    def grey_image(self, greypixellist):
        for pixel in greypixellist:
            self.image.putpixel((pixel.get_x_coordinates(), pixel.get_y_coordinates()), (pixel.get_red(), pixel.get_green(), pixel.get_blue()))
        return self.image

