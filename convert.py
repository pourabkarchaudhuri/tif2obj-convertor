import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Covert TIF sequence to OBJ Mesh')
    parser.add_argument('integers', metavar='Path', type=dir_path, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()
    args.func(args)