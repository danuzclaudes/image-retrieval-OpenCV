'''
Step1: define feature descriptor
1. convert to HSV and initialize features to quantify and represent the image
2. split by corners and elliptical mask
3. construct feature list by looping through corners and extending with center
'''

# import pkgs
import numpy as np
import cv2

#  extract 3D HSV color histogram from images
class FeatureDescriptor:
    def __init__(self, bins):
	# store # of bins for histogram
	self.bins = bins

    # convert RGB to HSV and 
    # initialize features to quantify and represent the image
    def describe(self, image):
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
	ellipse_mask = np.zeros(image.shape[:2], dtype = "uint8")
	cv2.ellipse(ellipse_mask, (cx, cy), (axesX, axesY), 0, 0, 360, 255, -1)

	# loop over mask corners
	for seg in segments:
		# construct mask for each corner by np.zeros()
		corner_mask = np.zeros(image.shape[:2], dtype = 'uint8')
		# draw rectangle mask on corner_mask object
		corner_mask[seg[0]:seg[1], seg[2]:seg[3]] = 255
		corner_mask = cv2.subtract(corner_mask, ellipse_mask)
		
		# extract hsv histogram	from segment of image with mask	
		hist = self.histogram(image, corner_mask)
		
		# update feature vector
		features.extend(hist)

	# extract hsv histogram from ellipse with mask
	hist_ellipse = self.histogram(image, ellipse_mask)
	features.extend(hist_ellipse)

	return features
    
    # Calculate the histogram of the masked region of the image
    def histogram(self,image, mask):
	# use number of bins per channel; 
	hist = cv2.calcHist([image],[0,1,2],mask,self.bins,[0,180,0,256,0,256])
	# normalize histogram to obtain scale invariance
	hist = cv2.normalize(hist).flatten()
	
	return hist
