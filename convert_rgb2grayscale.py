import os
from PIL import Image
from PIL import ImageOps
import argparse
import glob
import time

CURRENT_DIR = os.getcwd()

def execute_job(inputpath, outputpath):
    start_time = time.time()
    parts = os.path.split(inputpath)
    output_dir_name = parts[len(parts)-1]
    

    if not os.path.exists(os.path.join(CURRENT_DIR, outputpath, output_dir_name)):
        os.makedirs(os.path.join(CURRENT_DIR, outputpath, output_dir_name))

    filelist = glob.glob(os.path.join(CURRENT_DIR, inputpath, '*.tif'))

    for fn in filelist:  # For each name in the list
        print(fn)
        img = Image.open(fn).convert('L')
        # Resize each image
        size = 720 , 320
        im_resized = img.resize(size, Image.ANTIALIAS)
        
        fileparts = os.path.split(fn)
        
        output_file_name = os.path.join(CURRENT_DIR, outputpath, output_dir_name, fileparts[len(fileparts)-1])
        # img.convert('I;16').save(output_file_name)
        # Convert images to Binary
        binary = im_resized.point(lambda x: 0 if x<225 else 255, '1')  #binarization || x<225 is threshold value for binarization

        # Image Inversion
        inverted_image = ImageOps.invert( binary.convert('RGB') )
        inverted_image.save(output_file_name)
        
    execution_time = (time.time() - start_time)
    print("Grayscale Image Generation Execution time : {0:.2f}s".format(round(execution_time,2)))
    return
    

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Covert RGB TIF Images to Grayscale TIF Images')
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)

    args = parser.parse_args()
    print("Input Path : {} || Output Path : {}".format(args.input, args.output))
    # print(args.input)
    execute_job(args.input, args.output)

    print("Complete")