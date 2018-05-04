#A class to store information about pixels
class Pixel:

    def __init__(self, x, y, red, green, blue):
        self.coordinates = (x,y)
        self.rgb = {'red': red, 'green': green, 'blue': blue}
        self.rgb['red'] = red
        self.rgb['green'] = green
        self.rgb['blue'] = blue

    def get_coordinates(self):
        return self.coordinates

    def get_x_coordinates(self):
        return self.coordinates[0]

    def get_y_coordinates(self):
        return self.coordinates[1]

    def get_rgb(self):
        return self.rgb

    def get_red(self):
        return self.rgb['red']

    def get_green(self):
        return self.rgb['green']

    def get_blue(self):
        return self.rgb['blue']

