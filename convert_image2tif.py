# coding: utf-8
from __future__ import print_function # Python 2/3 compatibility
import glob
from PIL import Image
import tifffile
import numpy
import os
import argparse
import time

IMAGE_EXPORT_PATH = os.path.join(os.getcwd(), 'input')
# RAWX_DATASET_PATH = os.path.join(os.getcwd(), 'raw')
def PIL2array(img):
    """ Convert a PIL/Pillow image to a numpy array """
    return numpy.array(img.getdata(),
        numpy.uint8).reshape(img.size[1], img.size[0], 3)

def execute_job(folderpath):
    FRAMES = [] # Empty list of frames
    FIRST_SIZE = None # I am going to say that the first file is the right size
    # filelist = glob.glob("*.jpg") # For this test I am just using the images in the current directory in the order they are
    print(os.path.join(os.getcwd(), folderpath, '*.tif'))
    filelist = glob.glob(os.path.join(os.getcwd(), folderpath, '*.tif'))
    # Get the images into an array
    print("Filelist : {}".format(filelist))
    for fn in filelist:  # For each name in the list
        img = Image.open(fn) # Read the image
        if FIRST_SIZE is None:  # Don't have a size
            FIRST_SIZE = img.size  # So use this one
        if img.size == FIRST_SIZE: # Check the current image size if it is OK we can use it
            print ("Adding:", fn)  # Show some progress
            FRAMES.append(img)   # Add it to our frames list
        else:
            print ("Discard:", fn, img.size, "<>", FIRST_SIZE) # You could resize and append here!

    timestamp = str(time.time())
    macro_name = timestamp.split('.')
    
    OUT_NAME = "sequence_" + macro_name[0] + ".tif" # Name to save to
    OUT_PATH = os.path.join(IMAGE_EXPORT_PATH, OUT_NAME)
    print("Writing", len(FRAMES), "frames to", OUT_PATH)
    with tifffile.TiffWriter(OUT_PATH) as tiff:
        for img in FRAMES:
            tiff.save(PIL2array(img))
    # print("Done")

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Merge TIF images to TIF sequence')
    parser.add_argument('--path', required=True)

    args = parser.parse_args()
    if args.path == "":
        print("Blank")
    else:
        print("Folder path recieved : {}".format(args.path))
        execute_job(args.path)
    
        print("Complete")