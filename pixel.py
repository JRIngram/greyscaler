"""A class to store information about a pixel taken from an image"""
class Pixel:


    def __init__(self, x, y, red, green, blue):
        """Itialises the Pixel class
        
        Variables:
        
            coordinates: A tuple containing the coordinates of the pixel's location in the image it's taken from.
            
            rgb: An array to store the RGB values of each pixel.
            
            *     rgb['red'] = red values. e.g. an RGB value of (255,0,0) would return 255.
            
            *     rgb['green'] = green values. e.g. an RGB value of (0,255,0) would return 255.
            
            *     rgb['blue'] = blue values. e.g. an RGB value of (0,0,0255) would return 255.
    """
        self.coordinates = (x,y) 
        self.rgb = {'red': red, 'green': green, 'blue': blue}
        self.rgb['red'] = red
        self.rgb['green'] = green
        self.rgb['blue'] = blue

    def get_coordinates(self):
        """Returns the coordinates tuple
        """
        return self.coordinates

    def get_x_coordinates(self):
        """Returns the 'x' coordinates of the pixel
        """
        return self.coordinates[0]

    def get_y_coordinates(self):
        """Returns the 'y' coordinates of the pixel
        """
        return self.coordinates[1]

    def get_rgb(self):
        """Returns the rgb array
        """
        return self.rgb

    def get_red(self):
        """Returns the red value from the rgb array
        """
        return self.rgb['red']

    def set_red(self,red):
        """Sets the red value from the rgb array
        """
        self.rgb['red'] = red

    def get_green(self):
        """Returns the green value from the rgb array
        """
        return self.rgb['green']

    def set_green(self, green):
        """Sets the green value from the rgb array
        """
        self.rgb['green'] = green

    def get_blue(self):
        """Returns the blue value from the rgb array
        """
        return self.rgb['blue']

    def set_blue(self, blue):
        """Sets the blue value from the rgb array
        """
        self.rgb['blue'] = blue

