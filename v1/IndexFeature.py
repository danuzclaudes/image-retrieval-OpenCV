#!/usr/bin/python
# USAGE:
# python IndexFeature.py --dataset dataset --index index.csv

# import pkgs
import cv2
from FeatureDescriptor import *
import getopt, sys
import os

# parse arguments
try:
    optlist, args = getopt.getopt(sys.argv[1:],'',['dataset=','index='])
    # print optlist, args
except getopt.GetoptError as e:
    print (str(e))
    print 'Usage: %s --dataset path/to/dataset --index index.csv' % sys.argv[0]
    sys.exit(2)

data_dir = ''
idx_file = ''
for opt, val in optlist:
    if opt == '--dataset':
	data_dir = val
    if opt == '--index':
	idx_file = val

print data_dir, idx_file
print 

# initialize feature descriptor
# set bin = 16, H= 
feature_descriptor = FeatureDescriptor((8, 12, 3))

# read in list of filenames for all jpg images in directory
'''filepath = []
for f in os.listdir(data_dir): 
    if f.endswith('.png'):
        # print './dataset'+' '+f
	# print os.path.join(data_dir,f)
	filepath.append(os.path.join(data_dir, f))
print filepath

# write features to index file
output = open(idx_file, 'w')

for image_file in filepath:
    img = cv2.imread(image_file)
    
    # build index with file name
    print image_file
    
    # describe the image
    features = feature_descriptor.describe(img)
    output.write('%s\n' %features)'''

# read in all filenames from db
output = open(idx_file, 'w')
filepath = ''
for f in os.listdir(data_dir): '''for f in data_list'''
    if f.endswith('.png'):
	filepath = os.path.join(data_dir, f)
	#print filepath
	img = cv2.imread(filepath)

	imgID = f[:-4]
	#print type(f)
	#print fname
	# describe the image to produce features
	features = feature_descriptor.describe(img)
	
	print features	
	print

	# write id, features to output 
	'''write id, [feature] to db'''
	features = [str(f) for f in features]
	output.write('%s,%s\n' % (imgID, ','.join(features)))
	# note: join(list) can only accept lists of strings
	# needs to convert each item of features into str type

output.close()
