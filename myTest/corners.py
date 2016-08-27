#This is a simple open a picture and display it in gray scale.
import cv2
import numpy as np

img = cv2.imread("myTest.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 5000, 0.01, 10)
corners = np.int0(corners)

for corners in corners:
    x, y = corners.ravel()
    cv2.circle(img, (x,y), 3, 255, -1)

cv2.imshow('corners',img)
cv2.waitKey(0)
cv2.destroyAllWindows()