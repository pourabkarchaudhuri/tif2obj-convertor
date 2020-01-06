# coding: utf-8
from __future__ import print_function # Python 2/3 compatibility
import glob
from PIL import Image
import tifffile
import numpy
import os
import time
import argparse

# RAWX_DATASET_PATH = os.path.join(os.getcwd(), 'raw_grayscale')

def PIL2array(img):
    """ Convert a PIL/Pillow image to a numpy array """
    return numpy.array(img.getdata(), numpy.uint8).reshape(img.size[1], img.size[0], 3)
    # return numpy.array(img.getdata(), numpy.uint8)

def timestamp():
    x = str(time.time())
    x = x.split(".")
    x = "".join(x)
    return x

def execute_job(path):
    IMAGE_EXPORT_PATH = os.path.join(os.getcwd(), 'input')

    if not os.path.exists(IMAGE_EXPORT_PATH):
            os.makedirs(IMAGE_EXPORT_PATH)
    start_time = time.time()
    FRAMES = [] # Empty list of frames
    FIRST_SIZE = None # I am going to say that the first file is the right size

    full_foldername = os.path.split(path)
    only_foldername = full_foldername[len(full_foldername)-1]

    # macro_name = only_filename.split('.')
    # output_name = macro_name[0]

    OUT_NAME = only_foldername + ".tif" # Name to save to
    OUT_PATH = os.path.join(IMAGE_EXPORT_PATH, OUT_NAME)
    # filelist = glob.glob("*.jpg") # For this test I am just using the images in the current directory in the order they are
    filelist = glob.glob(os.path.join(os.getcwd(), path, '*.tif'))
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

    execution_time = (time.time() - start_time)
    print("TIF Sequence Generation Execution time : {0:.2f}s".format(round(execution_time,2)))
    return


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Covert TIF Binary dataset to TIF Sequence')
    parser.add_argument('--path', required=True)

    args = parser.parse_args()
    if args.path == "":
        print("Blank")
    else:
        print(args.path)
        execute_job(args.path)
    
        print("Complete")