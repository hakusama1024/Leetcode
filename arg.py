from argparse import ArgumentParser
import os.path


def is_valid_file(f):
    if not os.path.exists(f):
        print f, "not exist"
    else:
        print f, "exist" 


parser = ArgumentParser(description="test")
parser.add_argument("-i", dest="filename", required=True, help="input file name")
args = parser.parse_args()
print(type(args.filename))
is_valid_file(args.filename)



