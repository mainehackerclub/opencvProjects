#This will show 2 video windows, one in color and one in gray.
import cv2
import numpy as np

cap = cv2.VideoCapture(0)#0=1st capture device

while True: #Infinate loop
    ret, frame = cap.read() #ret means return is true/false.
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow("anyName",frame)
    cv2.imshow("gray",gray)#This video stream will be in gray

    if cv2.waitKey(1) & 0xff == ord('q'): # This uses q to exit from the infinite loop. Also without it I get one image.
        break

cap.release()
cv2.destroyAllWindows()