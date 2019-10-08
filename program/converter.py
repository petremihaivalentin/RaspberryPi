import sys
import numpy as np
import cv2

#using sys library for command-line arguments

blue = sys.argv[1]
green = sys.argv[2]
red = sys.argv[3]


#declaring the colored pixel in 8-bit format and converting it into HSV format  

color = np.uint8([[[blue, green, red]]])
hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

#grabbing the HSV values for the specific pixel

hue = hsv_color[0][0][0]

#output

print("Lower bound is :"),
print("[" + str(hue-10) + ", 100, 100]\n")

print("Upper bound is :"),
print("[" + str(hue + 10) + ", 255, 255]")