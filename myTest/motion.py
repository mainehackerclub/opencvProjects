#This is a simple show motion video

import cv2
import numpy as np


#function to take 3 images in a row, take the difference between the 1st and 2nd and the 2nd and 3rd.
#Then do an and to those two differences. The output is white where those two images are not the same.
def diffimg(a,b,c):
    t1=cv2.absdiff(a,b)
    t2=cv2.absdiff(b,c)
    t3=cv2.bitwise_and(t1,t2)
    return t3

#is this like setup in arduino
cap = cv2.VideoCapture(0)#0=1st capture device
#this must define the 3 different images.
t=cap.read(0)[1]
tp=cap.read(0)[1]
tpp=cap.read(0)[1]

#this converts the three images to gray
t = cv2.cvtColor(t,cv2.COLOR_BGR2GRAY)
tp = cv2.cvtColor(tp,cv2.COLOR_BGR2GRAY)
tpp = cv2.cvtColor(tpp,cv2.COLOR_BGR2GRAY)

while True:
    img = diffimg(t,tp,tpp)

    cv2.imshow("motion",img)

    res,img=cap.read()
    t=tp
    tp=tpp
    tpp = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


    k = cv2.waitKey(10)
    if k == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()