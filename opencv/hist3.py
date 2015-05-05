# grayscale histogram
# import pkgs
import cv2
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

# load image
img = cv2.imread('Lenna.png')

# convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# create histogram for grayscale
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(hist)
plt.xlim([0, 256])

plt.show() 
