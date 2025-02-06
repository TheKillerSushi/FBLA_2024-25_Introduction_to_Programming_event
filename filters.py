# BASIC FITLER APPLICATION
# SEE filter.py -h for more information

# START IMPORTS
from PIL import Image
import math
import random
import argparse
# END IMPORTS

# ALL filters below translate to a specific color palette via focusing specific colors in ( additive color mixing ?)
# ------ START BASE COLOR FILTERS ------ #
def gray_filter(image):
    size = image.size
    new_image = image
    for x in range(size[0]):
        for y in range(size[1]):
            pixel = image.getpixel((x,y))
            new_pixel_value = math.floor((pixel[0] + pixel[1] + pixel[2]) / 3)

            new_pixel = (new_pixel_value, new_pixel_value, new_pixel_value) # add , pixel[3] if using PNGS

            new_image.putpixel((x,y),new_pixel)
    return new_image
        

def sepia_filter(image):   
    size = image.size
    new_image = image
    for x in range(size[0]):
        for y in range(size[1]):
            pixel = image.getpixel((x,y))
            new_red = math.floor((pixel[0] * .393) + (pixel[1] * .769) + (pixel[2] * .189))
            new_green = math.floor((pixel[0] * .349) + (pixel[1] * .686) + (pixel[2] * .168))
            new_blue = math.floor((pixel[0] * .272) + (pixel[1] * .534) + (pixel[2] * .131))

            new_pixel = (new_red, new_green, new_blue)
            new_image.putpixel((x,y),new_pixel)
    return new_image

def yellow_filter(image):  
    size = image.size
    new_image = image
    for x in range(size[0]):
        for y in range(size[1]):
            pixel = image.getpixel((x,y))
        
            new_green = math.floor(pixel[1])
            new_blue = 0

            new_pixel = (pixel[0], new_green, new_blue)
            new_image.putpixel((x,y),new_pixel)
    return new_image


def blue_filter(image):
    size = image.size
    new_image = image
    for x in range(size[0]):
        for y in range(size[1]):
            pixel = image.getpixel((x,y))
        
            new_red = 0
            new_green = 0

            new_pixel = (new_red, new_green, math.floor(pixel[2]*.66))
            new_image.putpixel((x,y),new_pixel)
    return new_image



def dither(image): 
    size = image.size
    new_image = image
    for x in range(size[0]):
        for y in range(size[1]):
            pixel = image.getpixel((x,y))
            
    # DITHERS, rest of the algo is under if args["filter"]: around lines 350-380
            dither_change = 128
            Dither = math.floor(random.randint(0,dither_change) - dither_change/2)
            R = pixel[0] + Dither
            if R > 255: R = 255
            if R < 0: R = 0
            G = pixel[1] + Dither
            if G > 255: G = 255
            if G < 0: G = 0
            B = pixel[2] + Dither
            if B > 255: B = 255
            if B < 0: B = 0
    

            new_image.putpixel((x,y), pixel)
    return new_image
    #dither_multiplier = 1
    #dither_change_range = range(-(math.floor(dither_change*dither_multiplier)), (math.floor((dither_change*dither_multiplier)+1)))

    #current_pixel_gray = math.floor((pixel[0]+pixel[1]+pixel[2])/3)

    #current_pixel_gray = current_pixel_gray + int(current_pixel_gray*(random.choice(dither_change_range)/100))
        
    #if current_pixel_gray > 255:current_pixel_gray = 255
    #if current_pixel_gray < 0:current_pixel_gray = 0


    #new_pixel_color = (current_pixel_gray,current_pixel_gray,current_pixel_gray)


    #print(current_pixel_gray,"     ",new_pixel_gray)
    #return new_pixel_color

def blur(image):
    size = image.size
    # Blur via increasing kernel size 
    new_image = image
    size_of_kernel = 3

    for x in range(size[0]):
        for y in range(size[1]):
            current_pixel = image.getpixel((x,y))
            current_av = [0,0,0]
            count = 0
            numbers = []
            # Check and average the full kernel

            for x1 in range(size_of_kernel):
                if x - x1 > 0:
                    count += 1
                    new_pixel = image.getpixel((x-x1,y))
                    current_av[0] += new_pixel[0]
                    current_av[1] += new_pixel[1]
                    current_av[2] += new_pixel[2]
                
                if x + x1 < size[0]:
                    count += 1
                    new_pixel = image.getpixel((x+x1,y))
                    current_av[0] += new_pixel[0]
                    current_av[1] += new_pixel[1]
                    current_av[2] += new_pixel[2]
                
                for y1 in range(size_of_kernel):
                    if y - y1 > 0:
                        count += 1
                        new_pixel = image.getpixel((x,y-y1))
                        current_av[0] += new_pixel[0]
                        current_av[1] += new_pixel[1]
                        current_av[2] += new_pixel[2]
                        
                    if y + y1 < size[1]:
                        count += 1
                        new_pixel = image.getpixel((x,y+y1))
                        current_av[0] += new_pixel[0]
                        current_av[1] += new_pixel[1]
                        current_av[2] += new_pixel[2]
                        
                    
                    if y + y1 < size[1] and x + x1 < size[0]:
                        count += 1
                        new_pixel = image.getpixel((x+x1,y+y1))
                        current_av[0] += new_pixel[0]
                        current_av[1] += new_pixel[1]
                        current_av[2] += new_pixel[2]
                        
                    if y + y1 < size[1] and x - x1 > 0:
                        count += 1
                        new_pixel = image.getpixel((x-x1,y+y1))
                        current_av[0] += new_pixel[0]
                        current_av[1] += new_pixel[1]
                        current_av[2] += new_pixel[2]
                        
                    if y - y1 > 0 and x + x1 < size[0]:
                        count += 1
                        new_pixel = image.getpixel((x+x1,y-y1))
                        current_av[0] += new_pixel[0]
                        current_av[1] += new_pixel[1]
                        current_av[2] += new_pixel[2]
                        
                    if y - y1 > 0 and x - x1 > 0:
                        count += 1
                        new_pixel = image.getpixel((x-x1,y-y1))
                        current_av[0] += new_pixel[0]
                        current_av[1] += new_pixel[1]
                        current_av[2] += new_pixel[2]
                        
            count += 1
            current_av[0] = math.floor((current_av[0] + current_pixel[0]) / count)
            current_av[1] = math.floor((current_av[1] + current_pixel[1]) / count)
            current_av[2] = math.floor((current_av[2] + current_pixel[2]) / count)
            count = 0


                    #if count > 60:
                    #    print(len(numbers))

                        #print(numbers)
            new_image.putpixel((x,y),(current_av[0],current_av[1],current_av[2]))
            #print(count)
    return new_image

