 #This is a red color filtered picture using HSV  and cv2.bitwise_or()
import cv2
import numpy as np

raw   = cv2.imread("myTest.jpg")

hsv = cv2.cvtColor(raw,cv2.COLOR_BGR2HSV) #hsv is hue saturation value another way of looking at color than RBG or BRG.


lower_red = np.array([150,100,100])
upper_red = np.array([250,255,255])

maskhsv = cv2.inRange(hsv, lower_red, upper_red)
redhsv = cv2.bitwise_or(raw, raw, mask=maskhsv)

cv2.imshow("raw",raw)
cv2.imshow("redhsv",redhsv)

cv2.waitKey(0)
cv2.destroyAllWindows()
