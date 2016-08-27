#This doesn't work right.
import cv2
import numpy as np

cap = cv2.VideoCapture(0)  #0=1st capture device

while True:
    _, rawVideo = cap.read() #_ is an unused place holder
    gray =cv2.cvtColor(rawVideo,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(3,3),0)
    laplacian = cv2.Laplacian(blur,cv2.CV_64F)


    edges = cv2.Canny(blur, 100,100)
    # edgesLap = cv2.Canny(laplacian, 100,100)
    cv2.imshow("rawVideo",rawVideo) #rawVideo will be the title of the window.
    cv2.imshow("laplacian",laplacian)
    cv2.imshow("edges",edges)
    # cv2.imshow("edgesLap",edgesLap)




    keyPressed = cv2.waitKey(10)
    if keyPressed == 32:  #If q is pressed than the loop is exited. Some people use == 27 which means esc key.
        break

cap.release()
cv2.destroyAllWindows()
