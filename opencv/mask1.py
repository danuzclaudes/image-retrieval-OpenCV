# construct a mask for each corner of the image, 
# subtracting the elliptical center from it
# test cv2.rectangle(cornerMask, (startX, startY), (endX, endY), 255, -1)
import numpy as np
import cv2
import matplotlib
from matplotlib import pyplot as plt

image = cv2.imread('Lenna.png')

image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
(h, w) = image.shape[:2]
(cx, cy) = (int(w * 0.5), int(h * 0.5))

segments = [(0,cx, 0,cy)]

(axesX, axesY) = (int(w * 0.75) / 2, int(h * 0.75) / 2)
ellipMask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.ellipse(ellipMask, (cx, cy), (axesX, axesY), 0, 0, 360, 255, -1)

# pure black image of the same size as img object
cornerMask = np.zeros(image.shape[:2], dtype = "uint8")
print cornerMask
print cx,cy,cornerMask.shape

# cv2.rectangle does not return anything
cv2.rectangle(cornerMask,(0,0),(cx,cy),255, -1)
cornerMask = cv2.subtract(cornerMask,ellipMask)

cv2.imshow('show rect', cornerMask)
cv2.waitKey(0) 
