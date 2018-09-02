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

def rerun_program():
        rerun = None
        while(rerun != "y" and rerun != "n"):
            rerun = input("Would you like to greyscale using another algorithm? y/n\n> ")
            if(rerun == "y"):
                return True
            elif(rerun == "n"):
                return False
            else:
                print("Invalid input. Please enter 'y' to rerun the program or 'n' to exit the program.")
                
            
#Loads the original image
print("Loading image")
im = Image.open("img/test.jpg")
im.show()
print(im.format)
print(im.size)
print(im.mode)

def main(image):
    #Activates menu for user choice.
    algorithmChoice = algorithm_menu()

    if(algorithmChoice == "1"):
        print("Greyscale by average")
        image = Image.open("img/test.jpg")
        AVGGreyscale = GreyscaleByAverage(image, create_pixel_list(image))
        AVGGreyscale.grey_pixels()
        greyed = AVGGreyscale.get_averagedPixels()
        greyedImage = AVGGreyscale.grey_image()
        greyedImage.show()
        image.close()
        
    elif(algorithmChoice == "2"):
        print("Greyscale by max red")
        image = Image.open("img/test.jpg")
        maxRed = GreyscaleByMax(image, create_pixel_list(image), "red")
        maxRed.grey_pixels()
        greyed = maxRed.get_greyed_pixels()
        greyedImage = maxRed.grey_image()
        greyedImage.show()
        image.close()
        
    elif(algorithmChoice == "3"):
        print("Greyscale by max blue")
        image = Image.open("img/test.jpg")
        maxBlue = GreyscaleByMax(im, create_pixel_list(image), "blue")
        maxBlue.grey_pixels()
        greyed = maxBlue.get_greyed_pixels()
        greyedImage = maxBlue.grey_image()
        greyedImage.show()
        image.close()
        
    elif(algorithmChoice == "4"):
        print("Greyscale by max green")
        image = Image.open("img/test.jpg")
        maxGreen = GreyscaleByMax(image, create_pixel_list(image), "green")
        maxGreen.grey_pixels()
        greyed = maxGreen.get_greyed_pixels()
        greyedImage = maxGreen.grey_image()
        greyedImage.show()
        image.close()
        
    else:
        print("Invalid choice")
    
    if(rerun_program() == True):
        #Clears lists to stop memory leak.
        pixelList.clear()
        greyed.clear()
        main(im)

main(im)


