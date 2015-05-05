# Build an Image Retrieval System using Python and MySQL
This is a project for Independent Study in SILS.

# Acknowledgement
The key idea and main structure of the codes are from http://www.pyimagesearch.com/2014/12/01/complete-guide-building-image-search-engine-python-opencv/
Thanks to the site for sharing such a great tutorial for building a image search engine from scratch.

# /opencv
Before I start building up the system, some review on basic concepts in Computer Vision is essential. 
Thus, I come up with the OpenCV, a tool for fast prototyping of computer vision problems. 
OpenCV supports Python as library files; but more importantly, the official tutorial of OpenCV introduces basic 
concepts of computer vision through its example code snippets. 
Here are some of my learning results from OpenCV: 
 
● Image Handling and Pixel Accessing</p>
OpenCV provides a wide range of functions as of processing images. Through practical 
usage or invocation of these methods in Python, I gained a straightforward idea on pixels, 
RGB color space, bitmaps, gray­scale images and HSV color space. 
 
● Color Histogram </p>
Color histogram is a plot with pixel values (ranging from 0 to 255) in X­axis and corresponding 
number of pixels in the image on Y­axis. Histogram calculation in OpenCV is: </p>
</p>
<div><i>cv2.calcHist([images], channels, mask, histSize, ranges[, hist[, accumulate]]) </i></div>

# /v2
my version of codes in /v2 is a cleaner and revised version of the CBIR system.
It first utilizes different Python libraries (getopt) to parse the command line parameters. It also 
supports read/write with MySQL database, instead of simply processing I/O streams on disks 
(as csv files). 

</p>
<b>Step1: Define feature descriptor - FeatureDescriptor.py</b></p> 
The first step is to extract feature descriptors from training datasets. I’ve chosen color 
histograms as the feature and the generated feature vector can represent the original picture.  
 
Here’s the key idea of FeatureDescriptor.py: </p> 
1. convert to HSV and initialize features to quantify and represent the image </p> 
2. split by corners and elliptical mask </p> 
3. construct feature list by looping through corners and extending with center </p> 
 
<b>Step 2: Indexing features from dataset - featureExtraction.py</b></p> 
Now that we have our image descriptor defined, we can extract features (i.e. color 
histograms) from each image in our dataset. This process of extracting features and storing 
them into database is commonly called “indexing”. Thus, the index of all feature vectors, 
representing each image, is ready to be queried. 
 
Here’s the key idea of featureExtraction.py: </p> 
1. read in list of filenames for all jpg images in directory</p>  
2. write the path and name into database </p> 
3. extract features out using the feature descriptor and write each feature vector into database </p> 
 
<b>Step 3:  Retrieve index by query image - Retriever.py</b></p> 
This step aims to compute distances or similarities between given query feature vectors and 
indexed training feature vectors. Note that smaller distances implies more relevant images. 
We’ll return a dictionary of top­10 ranked images’ ids.  

Here’s the key idea of Retriever.py: </p> 
1. read all indices from db </p> 
2. compute distance of feature vectors between query and each row </p> 
3. sort the dictionary, return a tuple of (id, distance) </p> 
 
<b>Step 4: Retrieval system design - retrieveIndex.py</b></p> 
 
Here’s the key idea of retrieveIndex.py: </p> 
1. extract feature from query image </p> 
2. perform retrieval through index table </p> 
3. loop over results of retrieved top limit image and display the result</p> 
