'''Below program loads an image in grayscale, 
displays it, save the image if you press 's' and exit, 
or simply exit without saving if you press ESC key.'''

import numpy as np
import cv2

img = cv2.imread('Lenna.png')
cv2.imshow('original', img)
k = cv2.waitKey(0) & 0xFF
h, w = img.shape[:2]

white1 = img
white1[0:10, 0:10] = 255

white2 = img
white2[int(w/2):, int(h/2):] = 255

k = cv2.waitKey(0) & 0xFF
while(k != 27):
  if k == ord('s'): # wait for 's' key to save and exit
    k = cv2.destroyAllWindows()
    cv2.imwrite('Lenna_gray.png',img)
  elif k == ord('a'):
    k = cv2.destroyAllWindows()
    cv2.imshow('white1', white1)
  elif k == ord('b'):
    k = cv2.destroyAllWindows()
    cv2.imshow('white2', white2)
  k = cv2.waitKey(0) & 0xFF

k = cv2.destroyAllWindows()
