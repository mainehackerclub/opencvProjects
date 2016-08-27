#This is a simple capture video
import cv2
import numpy as np

cap = cv2.VideoCapture(0)#0=1st capture device

while (cap.isOpened()):
    ret, frame = cap.read() #ret means return is true/false.
    cv2.imshow("anyName",frame)

    k = cv2.waitKey(10)
    if k == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
