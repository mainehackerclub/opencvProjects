#This is a simple open a picture and display it in gray scale.
import cv2
import numpy as np

img = cv2.imread("myTest.jpg", cv2.IMREAD_GRAYSCALE)
raw = cv2.imread("myTest.jpg")

mat = cv2.split(raw,[3])
mat[1]=mat[2]
merged = cv2.merge(mat,3)

cv2.imshow('raw',raw)
cv2.imshow('gray',img)

cv2.imshow('matBlue',mat[0])
cv2.imshow('matGreen',mat[1])
cv2.imshow('matRed',mat[2])
cv2.imshow('merged',merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
