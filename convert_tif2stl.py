"""
Example to read volumetric data in the form of a tiff stack
or SLC (StereoLithography Contour) from files
with or without automatic isosurfacing:

A tiff stack is a set of image slices in z. The scalar value
(intensity of white) is used to create an isosurface by fixing a threshold.
If threshold=None this is set to 1/3 of the scalar range.

- If the spacing of the tiff stack is uneven in xyz, this can be
fixed by setting scaling factors with scaling=[xfac,yfac,zfac]
"""
# print(__doc__)
import time

# Import Dependencies
from vtkplotter import show, load, save
import vtkplotter.vtkio as exp
import os
import time
# Set Filepath



def timestamp():
    x = str(time.time())
    x = x.split(".")
    x = "".join(x)
    return x

def convert(path):
    EXPORT_PATH = os.path.join(os.getcwd(), "output", "stl")

    if not os.path.exists(EXPORT_PATH):
            os.makedirs(EXPORT_PATH)
    
    start_time = time.time()
    # print("Relative obtained {}".format(path))
    # FILE_NAME = "test.tif"
    # FILE_PATH = os.path.join(INPUT_PATH, FILE_NAME)
    FILE_PATH = os.path.join(os.getcwd(), path)
    # print("Absolute obtained {}".format(FILE_PATH))
    # Set Params
    THRESHOLD = 80

    # Load Data
    # v = load(FILE_PATH) # Volume
    a = load(FILE_PATH, threshold=THRESHOLD) # isosurfacing on the fly
    print("Loading TIF Stack")
    # vp1 = show(v, a, shape=(1, 2), axes=8, viewup='z')
    # save(a, "output.obj", binary=True)
    full_filename = os.path.split(path)
    only_filename = full_filename[len(full_filename)-1]

    macro_name = only_filename.split('.')
    output_name = macro_name[0]

    # Save Path
    EXPORT_NAME = output_name + ".stl"
    # macro_name = FILE_NAME.split('.')
    # EXPORT_NAME = macro_name[0] + ".stl"
    EXPORT_FILE = os.path.join(EXPORT_PATH, EXPORT_NAME)
    exp.write(a, EXPORT_FILE, binary=True)
    execution_time = (time.time() - start_time)
    print("Export to .STL completed")
    print("STL Generation Execution time : {0:.2f}s".format(round(execution_time,2)))
    return EXPORT_NAME

