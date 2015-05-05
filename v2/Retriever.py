'''
Step 3: Retrieve index by query image
1. read all indices from db
2. compute distance of feature vectors between query and each row
3. sort the dictionary, return a tuple of (id, distance)
'''
#!/usr/bin/python
import math
import operator
import csv
from Index import *

class Retriever:
    def __init__(self):
	print "retriever begin to search Index"
    
    def search(self, query, limit):
	# build a new idictionary
	distances = {}

	# read all index from db
	index_obj = Index()
	data_list = index_obj.read_all_features_from_Index()

	# loop over rows in data list
	# and compute distance between query and row's feature
	for fid, feature in data_list:
	    # extract features out from csv and convert back to numeric
	    features = [float(x) for x in feature.strip('[]').split(',')]
	    
	    # compute distance between query and row's feature
	    dist = self.calc_distance(features, query)
	    distances[fid] = dist
	
	print "all distances from query as dict:"
	print distances
	
	# sort the dictionary, return a list of tuples (id, distance)
	# smaller distances implies more relevant images
	distances = sorted(distances.items(), key=operator.itemgetter(1))
	print "sorted distances as list of tuple:"
	print distances

	# return top k records
	return distances[:limit]

    def calc_distance(self, features, query):
	# compute euclidean distance
	return math.sqrt(sum([(x-y)**2 for x,y in zip(features, query)]))	
	
