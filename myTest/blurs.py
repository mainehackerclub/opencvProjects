#This is a red color filtered video with some blurs
import cv2
import numpy as np

cap = cv2.VideoCapture(0)#0=1st capture device

while True:
    _, frame = cap.read() #ret means return is true/false.  #The underscore is used a place holder.

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)  #hsv is hue saturation value another way of looking at color than RBG or BGR.
    lower_red = np.array([150,50,10])
    upper_red = np.array([175,100,100])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    red = cv2.bitwise_and(frame, frame, mask=mask)

    gaussBlur = cv2.GaussianBlur(red,(15,15),0)
    median = cv2.medianBlur(red,15)


    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("red",red)
    cv2.imshow("gaussBlur",gaussBlur)
    cv2.imshow("median",median)


    k = cv2.waitKey(10)
    if k == 32:
        break

cap.release()
cv2.destroyAllWindows()
