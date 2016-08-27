 #This is a red color filtered video
import cv2
import numpy as np

cap = cv2.VideoCapture(0)#0=1st capture device

while True:
    _, raw = cap.read()  #The underscore is used a place holder.

    hsv = cv2.cvtColor(raw,cv2.COLOR_BGR2HSV)  #hsv is hue saturation value another way of looking at color than RBG or BGR.

    lower_red = np.array([100,  100, 100])
    upper_red = np.array([255, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)


    red = cv2.bitwise_and(hsv, hsv, mask=mask)

    cv2.imshow("raw",raw)
    cv2.imshow("mask",mask)
    cv2.imshow("red",red)

    k = cv2.waitKey(100)
    if k == 32: # spacebar
        break

cap.release()
cv2.destroyAllWindows()
