from PIL import Image
import pixel
import greyscale_by_average

Pixel = pixel.Pixel
GreyscaleByAverage = greyscale_by_average.GreyscaleByAverage
pixelList = []




def create_pixel_list(image):
    for x in range(0, image.size[0]):
        for y in range(0, image.size[1]):
            imagepixel = im.getpixel((x,y))
            #print("red:" + str(imagepixel[0]) + " green:" + str(imagepixel[1]) + " blue: " + str(imagepixel[2]))
            list_pixel = Pixel(x, y, imagepixel[0], imagepixel[1], imagepixel[2])
            #print(list_pixel.get_coordinates())
            #print(list_pixel.get_rgb())
            pixelList.append(list_pixel)
    return pixelList


'''
Currently uses the averaging greyscale algorithm.
Used as a proof-of-concept. 
This is likely to be refactored to its own module along with more algorithms to allow the user to choose which greyscale algorithm to use.

def greyscale_image(image):
    for pixel in pixelList:
        average = round((pixel.get_red() + pixel.get_green() + pixel.get_blue()) / 3)
        image.putpixel((pixel.get_x_coordinates(), pixel.get_y_coordinates()), (average, average, average))
        print("AVERAGE = " + str(average) + "\n")
    return image
'''


#Loads the original image
print("Loading image")
im = Image.open("img/test.jpg")
im.show()
print(im.format)
print(im.size)
print(im.mode)


AVGGreyscale = GreyscaleByAverage(im, create_pixel_list(im))
AVGGreyscale.grey_pixels()
greyed = AVGGreyscale.get_averagedPixels()
greyedImage = AVGGreyscale.grey_image()
greyedImage.show()








