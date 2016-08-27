# Takes a pixel from a location on an image and prints the BRG and HSV values and draws a dot at that location.
import cv2
import numpy as np

img   = cv2.imread("myTest.jpg")
x=300
y=600
px = img[x,y]
print"BRG  ",px

hsv =cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
px = hsv[x,y]
print "HSV   " ,px

cv2.circle(img, (x,y), 3, 255, -1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
