#This is a simple capture video
import cv2
import numpy as np

cap = cv2.VideoCapture(0)#0=1st capture device
fgbg = cv2.BackgroundSubtractorMOG2()  #the original code didn't work which was cv2.createBackgroundSubtractorMOG2()


while True:

    _, frame = cap.read() #_ is an unused place holder
    fgmask = fgbg.apply(frame)

    cv2.imshow("rawVideo",frame) #rawVideo will be the title of the window.


    cv2.imshow('fqmask',fgmask)
    keyPressed = cv2.waitKey(10)
    if keyPressed == 32:  #I sb is pressed than the loop is exited. Some people use == 27 which means esc key.
        break

cap.release()

cv2.destroyAllWindows()
