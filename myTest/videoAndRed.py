#This is a simple capture video plus a window with red.
import cv2
import numpy as np

cap = cv2.VideoCapture(0)#0=1st capture device

while (cap.isOpened()):
    ret, frame = cap.read() #ret means return is true/false.
    cv2.imshow("anyName",frame)

    #This is the blue/green/red range. If all 3 colors are within the range it will show as white else black.
    red = cv2.inRange(frame,cv2.cv.Scalar(0,100,100),cv2.cv.Scalar(255,200,200))
    cv2.imshow("red",red)

    k = cv2.waitKey(10)
    if k == 32:
        break

cap.release()
cv2.destroyAllWindows()
