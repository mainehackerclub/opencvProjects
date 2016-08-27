 #This is a red color filtered video
import cv2
import numpy as np

cap = cv2.VideoCapture(0)#0=1st capture device

while True:
    _, frame = cap.read() #ret means return is true/false.  #The underscore is used a place holder.

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)  #hsv is hue saturation value another way of looking at color than RBG or BGR.
    lower_red = np.array([150,100,100])
    upper_red = np.array([250,255,255])

    mask = cv2.inRange(hsv, lower_red, upper_red)

    red = cv2.bitwise_or(frame, frame, mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("red",red)

    k = cv2.waitKey(10)
    if k == 32:
        break

cap.release()
cv2.destroyAllWindows()
