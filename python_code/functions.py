from os import path as opath
import sys

def get_data(problem_number):
    path = opath.abspath(opath.dirname(sys.argv[0]))

    relative_filename = 'no%s.txt' % str(problem_number).zfill(3)
    relative_path = "/".join(["..",
                              "..",
                              "problem_data",
                              relative_filename])

    filename = opath.join(path, relative_path)
    with open(filename) as fh:
        # files if file doesn't exist
        result = fh.read()
    return result
