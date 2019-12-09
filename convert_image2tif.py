# coding: utf-8
from __future__ import print_function # Python 2/3 compatibility
import glob
from PIL import Image
import tifffile
import numpy
import os

IMAGE_EXPORT_PATH = os.path.join(os.getcwd(), 'input')
RAWX_DATASET_PATH = os.path.join(os.getcwd(), 'raw')
def PIL2array(img):
    """ Convert a PIL/Pillow image to a numpy array """
    return numpy.array(img.getdata(),
        numpy.uint8).reshape(img.size[1], img.size[0], 3)
FRAMES = [] # Empty list of frames
FIRST_SIZE = None # I am going to say that the first file is the right size
OUT_NAME = "test.tif" # Name to save to
OUT_PATH = os.path.join(IMAGE_EXPORT_PATH, OUT_NAME)
# filelist = glob.glob("*.jpg") # For this test I am just using the images in the current directory in the order they are
filelist = glob.glob(os.path.join(RAWX_DATASET_PATH, 'raw_dataset_1', '*.tif'))
# Get the images into an array
for fn in filelist:  # For each name in the list
    img = Image.open(fn) # Read the image
    if FIRST_SIZE is None:  # Don't have a size
        FIRST_SIZE = img.size  # So use this one
    if img.size == FIRST_SIZE: # Check the current image size if it is OK we can use it
        print ("Adding:", fn)  # Show some progress
        FRAMES.append(img)   # Add it to our frames list
    else:
        print ("Discard:", fn, img.size, "<>", FIRST_SIZE) # You could resize and append here!

print("Writing", len(FRAMES), "frames to", OUT_PATH)
with tifffile.TiffWriter(OUT_PATH) as tiff:
    for img in FRAMES:
        tiff.save(PIL2array(img))
print("Done")