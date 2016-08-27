#Subtracts the not moving background from the image and puts a mask of the moving objects.

import numpy as np
import cv2


cap = cv2.VideoCapture('people-walking.mp4')

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
fgbg = cv2.BackgroundSubtractorMOG2()  #the original code didn't work which was cv2.createBackgroundSubtractorMOG2()

while   True:
    _ , frame   = cap.read()


    fgmask = fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    cv2.imshow('frame',frame)
    cv2.imshow('fgmask',fgmask)



    k = cv2.waitKey(30)
    if k == 32:
        break


cap.release()
cv2.destroyAllWindows()
