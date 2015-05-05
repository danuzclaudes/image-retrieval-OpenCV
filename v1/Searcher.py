#!/usr/bin/python
import math
import operator
import csv

class Searcher:
    def __init__(self, index_file):
	# store index path:
	self.index_file = index_file
    
    def search(self, query, limit):
	# build a new idictionary
	distances = {}

	# open index file for reading  
	'''read all index from db'''
	indexCSV = open(self.index_file, 'r')
	reader = csv.reader(indexCSV)

	# loop over rows in index.csv
	# compute distance between query and row's feature
	for row in reader:
	    # extract features out from csv and convert back to numeric
	    features = [float(x) for x in row[1:]]
	    dist = self.calc_distance(features, query)
	    distances[row[0]] = dist
	
	print "all distances from query as dict:"
	print distances
	indexCSV.close()
	
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
	
