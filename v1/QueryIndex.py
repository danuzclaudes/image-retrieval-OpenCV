#!/usr/bin/python
# usage
# python QueryIndex.py --index index.csv --query 106600.png --result-path dataset

# import pkgs
import cv2
from FeatureDescriptor import *
from Searcher import *

import sys
import getopt

# parse command line argument
# print sys.argv[1:] # for debugging
try:
    (optlist, args) = getopt.getopt(sys.argv[1:],'',['index=','query=','result-path='])
except getopt.GetoptError as e:
    print (str(e))
    print 'Usage: %s --index index.csv --query query_image --result-path dataset' % sys.argv[0]
    sys.exit(2)

# store argument into variables
index_file=''
query_file=''
result_path=''
for opt, val in optlist:
    if opt == '--index':
	index_file = val
    elif opt == '--query':
	query_file = val
    else:
	result_path = val

# extract feature from query image
query_img = cv2.imread(query_file)
feature_descriptor = FeatureDescriptor((8,12,3))
query_features = feature_descriptor.describe(query_img)

# perform retrieval through index file # retrieves db
searcher = Searcher(index_file)
retrieval_results = searcher.search(query_features, limit=10)

# display query image
cv2.imshow("Query", query_img)

# loop over results of retrieved top limit image
for(id, distance) in retrieval_results:
    result = cv2.imread(result_path+'/'+id+'.png')
    print result
    print result_path+'/'+id+'.png'
    cv2.imshow("Result",result)
    cv2.waitKey(0)
