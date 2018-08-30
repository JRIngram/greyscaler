from PIL import Image
import pixel
import greyscale_by_average
import greyscale_by_max

Pixel = pixel.Pixel
GreyscaleByAverage = greyscale_by_average.GreyscaleByAverage
GreyscaleByMax = greyscale_by_max.GreyscaleByMax
pixelList = []

def algorithm_menu():
    validOptions = ["1", "2", "3", "4"]
    print("Enter the corresponding number for the algorithm you would like to use to greyscale the image:")
    print("\t1 Greyscale by average")
    print("\t2 Greyscale by maximising red values.")
    print("\t3 Greyscale by maximising blue values.")
    print("\t4 Greyscale by maximising green values.")
    choice = input("> ")
    while(choice not in validOptions):
        print("Invalid option selected. Please enter a valid number.\ne.g. if you would like to greyscale by average enter '1'")
        choice = input("> ")
    return choice
    


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


#Activates menu for user choice.
algorithmChoice = algorithm_menu()
if(algorithmChoice == "1"):
    print("Greyscale by average")
elif(algorithmChoice == "2"):
    print("Greyscale by max red")
elif(algorithmChoice == "3"):
    print("Greyscale by max blue")
elif(algorithmChoice == "4"):
    print("Greyscale by max green")
else:
    print("Invalid choice")

#Loads the original image
print("Loading image")
im = Image.open("img/test.jpg")
im.show()
print(im.format)
print(im.size)
print(im.mode)





'''
im = Image.open("img/test.jpg")
# Greyscale by averaging
AVGGreyscale = GreyscaleByAverage(im, create_pixel_list(im))
AVGGreyscale.grey_pixels()
greyed = AVGGreyscale.get_averagedPixels()
greyedImage = AVGGreyscale.grey_image()
greyedImage.show()
im.close()


# Greyscale by maxing green
im = Image.open("img/test.jpg")
maxGreen = GreyscaleByMax(im, create_pixel_list(im), "green")
maxGreen.grey_pixels()
greyed = maxGreen.get_greyed_pixels()
greyedImage = maxGreen.grey_image()
greyedImage.show()
im.close()
'''
#Greyscale by maxing red
im = Image.open("img/test.jpg")
maxRed = GreyscaleByMax(im, create_pixel_list(im), "red")
maxRed.grey_pixels()
greyed = maxRed.get_greyed_pixels()
greyedImage = maxRed.grey_image()
greyedImage.show()
im.close()

# Greyscale by maxing blue
im = Image.open("img/test.jpg")
maxBlue = GreyscaleByMax(im, create_pixel_list(im), "blue")
maxBlue.grey_pixels()
greyed = maxBlue.get_greyed_pixels()
greyedImage = maxBlue.grey_image()
greyedImage.show()
im.close()
