#This is a simple open a picture and display edges.
import cv2
import numpy as np
raw = cv2.imread("myTest.jpg")
img = cv2.imread("myTest.jpg", cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(img,200,200)
edgesBGR= cv2.cvtColor(edges,cv2.COLOR_GRAY2BGR)
rawEdges = cv2.add(raw,edgesBGR)

cv2.imshow('image',img)

cv2.imshow('edges',edges)
cv2.imshow('rawEdges',rawEdges)
cv2.waitKey(0)
cv2.destroyAllWindows()
