from greyscale_algorithm import GreyscaleAlgorithm
from enum import Enum
import copy

class GreyscaleByMax(GreyscaleAlgorithm):
    colourToMax = ""
    greyedPixels = []
    
    def __init__(self, image, pixelList, colourToMax):
        GreyscaleAlgorithm.__init__(self, image, pixelList)
        if(colourToMax.upper() == "RED" or colourToMax.upper() == "GREEN" or colourToMax.upper() == "BLUE"):
            self.colourToMax = colourToMax.upper()
        else:
            print("An error has occurred.\nNo valid colour selected.\nDefaulting to max = red.")
            self.colourToMax = "RED"



    def grey_pixels(self):
        greyedPixels = []
        pixels = []
        for pixel in self.pixelList:
            maxedPixel = copy.copy(pixel)
            pixels.append(pixel)
            if(self.colourToMax == "RED"):
                maxedPixel.set_green(maxedPixel.get_red())
                maxedPixel.set_blue(maxedPixel.get_red())
            elif(self.colourToMax == "GREEN"):
                maxedPixel.set_red(maxedPixel.get_green())
                maxedPixel.set_blue(maxedPixel.get_green())
            elif(self.colourToMax == "BLUE"):
                maxedPixel.set_red(maxedPixel.get_blue())
                maxedPixel.set_green(maxedPixel.get_blue())
            greyedPixels.append(maxedPixel)

        self.greyedPixels = greyedPixels

    def get_greyed_pixels(self):
        return self.greyedPixels

    def grey_image(self):
        return super(GreyscaleByMax, self).grey_image(self.greyedPixels)
