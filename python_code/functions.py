from os.path import expanduser
from os.path import join

def get_data(problem_number):
    relative_filename = 'no%s.txt' % str(problem_number).zfill(3)
    path = "/".join(["..",
                     "..",
                     "problem_data"])
    filename = join(expanduser(path), relative_filename)
    with open(filename) as fh:
        # files if file doesn't exist
        result = fh.read()
    return result
