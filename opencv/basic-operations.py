import cv2
import numpy

import os
os.listdir('./')

img = cv2.imread('Lenna.png')

px = img[100,200]
print px

# access only blue pixel of a BGR image
blue = img[100,200,0]
# modeify pixel value
img[100,200] = [255,255,255]
print img[100,200]

# access and modify pixel values through array.item() and array.itemset()
img.item(100,200,2) # access RED value
img.itemset((100,200,2), 88) # modify RED value

# access image properties
print img.shape # returns a tuple of number of row, cols and channels

print img.size # show total number of pixels

print img.dtype # show image datatype

# split and merge image channels
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

# Numpy indexing
img[:,:,2] = 0 # set all red pixels to zero

