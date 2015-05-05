#!/usr/bin/python
# test db funcionality

from Index import *
import os

index_obj = Index()

data_dir = './dataset'

#index_obj.write_img_path_into_Image(data_dir)

data = index_obj.read_img_path_from_Image()
# print data

#feature = [0.20870997, 0.0012804293, 0.0, 0.01920644, 0.00076825754]
#index_obj.write_all_features_into_Index(feature)
'''
for f in data:
    # print f[0],f[1] ./dataset/xxx.png 101000
    feature = [0.20870997, 0.0012804293, 0.0, 0.01920644, 0.00076825754]
    index_obj.write_all_features_into_Index(f[1],feature)
'''

data = index_obj.read_all_features_from_Index()
# note: data is a tuple of strings ('10001', '[...]')

for fid, feature in data:
    print feature 
    # note: feature is string formatted list => '[v1,v2,v3]'
    feature = [float(x) for x in feature.strip('[]').split(',')]
    print feature
