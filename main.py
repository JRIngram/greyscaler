from PIL import Image


'''
Currently uses the averaging greyscale algorithm.
Used as a proof-of-concept. 
This is likely to be refactored to its own module along with more algorithms to allow the user to choose which greyscale algorithm to use.
'''
def greyscale_image(image):
    for x in range(0, image.size[0]):
        for y in range(0, image.size[1]):
            print("(" + str(x) + "," + str(y) + ")")
            pixel = image.getpixel((x,y))
            average = round((pixel[0] + pixel[1] + pixel[2]) / 3)
            print("AVERAGE = " + str(average) + "\n")
            image.putpixel((x, y), (average, average, average))
    return image

#Loads the original image
print("Loading image")
im = Image.open("img/test.jpg")
im.show()
print(im.format)
print(im.size)
print(im.mode)

#Loads the greyscaled image.
greyrgb = greyscale_image(im)
greyrgb.show()
print(greyrgb.getpixel((0, 639)))
print(greyrgb.getpixel((639, 639)))
print(greyrgb.getpixel((639, 0)))
print(greyrgb.getpixel((0, 0)))




