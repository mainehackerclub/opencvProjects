#This is a simple capture video
import cv2
import numpy as np

cap = cv2.VideoCapture(0)  #0=1st capture device

while True: #Infinate loop
    ret, frame = cap.read() #ret means return is trun/false.
    cv2.imshow("anyName", frame)

    if cv2.waitKey(1) & 0xff == ord('q'): # This uses q to exit from the infinite loop. Also without it I get one image.
        break

cap.release()
cv2.destroyAllWindows()

