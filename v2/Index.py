#!/usr/bin/python
# Index Class would support :
# 0. write all img path  in the directory into Image Table
# 1. read all img path from Image Table
# 2. write all features into Index Table
# 3. read all freatures from Index Table
import MySQLdb
import os
import traceback

class Index:
    #def __init__(self):
    #	# dont need init if no para needed?
    
    def write_img_path_into_Image(self, dataset):
	db=MySQLdb.connect("localhost","root","333666","image_retrieval")
	cursor=db.cursor()
	
	filepath=''
	for fid,f in enumerate(os.listdir(dataset)):
	    if f.endswith('.png'):
		fid=f[:-4]
		filepath = os.path.join(dataset, f)
		# print fid,f[:-4],filepath
		sql="""insert into Image (img_id, filepath) \
values ('{0}','{1}');""".format(str(fid), filepath)
		print sql
		try:
		    # execute sql statement
		    cursor.execute(sql)
		    db.commit() # commit changes in db
		except Exception:
		    db.rollback() # rollback in case error
		    print "Error: Unable to write into Image"
		    print traceback.format_exc()
	# disconnect from server
	db.close()

    def read_img_path_from_Image(self):
	db = MySQLdb.connect("localhost","root","333666","image_retrieval")
	cursor = db.cursor()
	sql="""select * from Image;"""

	try:
	    cursor.execute(sql)
	    data = cursor.fetchall()
	except:
	    "Error: Unable to fetch data from Image"

	# print data
	# disconnect from server
	db.close()
	return data

    def write_all_features_into_Index(self, fid, feature):
	feature = str(feature)
	
	db=MySQLdb.connect("localhost","root","333666","image_retrieval")
	cursor=db.cursor()

	sql="insert into ImageIndex (fid, feature) \
values ('{0}','{1}')".format(fid,feature)
	#print sql
	try:
	    cursor.execute(sql)
	    db.commit()
	except Exception:
	    db.rollback()
	    print traceback.format_exc()
	db.close()

    def read_all_features_from_Index(self):
	db=MySQLdb.connect("localhost","root","333666","image_retrieval")
	cursor=db.cursor()

	sql="select * from ImageIndex;"
	try:
	    cursor.execute(sql)
	    data = cursor.fetchall()
	except Exception:
	    print traceback.format_exc()
	db.close()
	return data




