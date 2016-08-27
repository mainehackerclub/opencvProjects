#This is a simple capture video
import cv2
import numpy as np

cap = cv2.VideoCapture(0)#0=1st capture device

while True:
    _, rawVideo = cap.read() #_ is an unused place holder




    cv2.imshow("rawVideo",rawVideo) #rawVideo will be the title of the window.


    keyPressed = cv2.waitKey(10)  #I don't know what the different waitKey arguments are.
    if keyPressed == 32:  #If spacebar is pressed than the loop is exited. Some people use == 27 which means esc key.
        break

cap.release()
cv2.destroyAllWindows()
