import argparse

def execute_job(filepath):
    print("Found Input at : {}".format(filepath))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Covert TIF sequence to OBJ Mesh')
    parser.add_argument('--path', required=True)

    args = parser.parse_args()
    print(args.path)
    execute_job(args.path)