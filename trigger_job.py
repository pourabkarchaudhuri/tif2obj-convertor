import argparse
import convert_tif2stl
import convert_stl2obj
import os



def execute_job(path):
    OUTPUT_EXPORT_PATH = os.path.join(os.getcwd(), 'output')

    if not os.path.exists(OUTPUT_EXPORT_PATH):
            os.makedirs(OUTPUT_EXPORT_PATH)
    # print("Input at : {}".format(path))
    
    STL_PATH = convert_tif2stl.convert(path)

    OBJ_PATH = convert_stl2obj.convert(STL_PATH)
    print("Final .OBJ filename : {}".format(OBJ_PATH))
    return


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Covert TIF sequence to OBJ Mesh')
    parser.add_argument('--path', required=True)

    args = parser.parse_args()
    if args.path == "":
        print("Blank")
    else:
        print(args.path)
        execute_job(args.path)
    
        print("Complete")