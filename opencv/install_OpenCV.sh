version="$(wget -q -O - http://sourceforge.net/projects/opencvlibrary/files/opencv-unix | egrep -m1 -o '\"[0-9](\.[0-9]+)+' | cut -c2-)"

echo $version

mkdir ../OpenCV
cd ../OpenCV

sudo apt-get install build-essential cmake libgtk2.0-dev pkg-config python-dev libavcodec-dev libavformat-dev libswscale-dev
sudo pip install numpy

# PRE: OpenCV downloaded
$ unzip opencv-2.4.9.zip
$ cd opencv-2.4.9
$ mkdir build
$ cd build

cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D BUILD_NEW_PYTHON_SUPPORT=ON ..

make
sudo make install

cd ../../../ # return to root of virtualenv dir
source ./bin/activate 
pip install numpy

cd lib
cp /usr/local/lib/python2.7/dist-packages/cv2.so ./python2.7/site-packages

cd ..
# rm -rf OpenCV or the opencv-2.4.x dir

ldd /usr/local/lib/python2.7/dist-packages/cv2.so

echo "OpenCV" $version "ready to be used"


