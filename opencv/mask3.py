import numpy as np
import matplotlib
import cv2

image = cv2.imread('Lenna.png')

# convert RGB to HSV and initialize fatures to quantify and represent the image
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
features = []

# grab dimensions and computer center of image
# from beginning 0 to end-1 = 1, i.e. shape[0] & shape[1]
(h, w) = image.shape[:2]
(cx, cy) = (int(w * 0.5), int(h * 0.5))

# divide image into top-left, top-right, bottom-right, bottom-left corner segments as mask
segments = [(0,cx,0,cy), (0,cx,cy,h), (cx,w,cy,h), (cx,w,0,cy)]

# construct an elliptical mask representing the center of the image
(axesX, axesY) = (int(w * 0.75) / 2, int(h * 0.75) / 2)
ellipMask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.ellipse(ellipMask, (cx, cy), (axesX, axesY), 0, 0, 360, 255, -1)

# loop over mask corners
for seg in segments:
	# construct mask for each corner by cv2.bitwise_and()
	corner_mask = np.zeros(image.shape[:2], dtype = 'uint8')
	# draw rectangle mask on corner_mask object
	corner_mask[seg[0]:seg[1], seg[2]:seg[3]] = 255
	print corner_mask
	corner_mask = cv2.subtract(corner_mask, ellipMask)
	print corner_mask
	cv2.imshow('segment', corner_mask)
	cv2.waitKey(0)

	hist = cv2.calcHist([image], [0, 1, 2], corner_mask,(8, 12, 3),[0, 180, 0, 256, 0, 256])
	print hist
	
