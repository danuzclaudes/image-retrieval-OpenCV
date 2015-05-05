import cv2
import numpy as np
# import Tkinter
import matplotlib
# matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

img = cv2.imread('Lenna.png')

color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.title('Color Histogram')
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()
