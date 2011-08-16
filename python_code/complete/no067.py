#!/usr/bin/env python

# By starting at the top of the triangle below and moving to adjacent
# numbers on the row below, the maximum total from top to bottom is
# 23. (3 -> 7 -> 4 -> 9)
# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in no067.txt, a 15K text file
# containing a triangle with one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18. It is not possible
# to try every route to solve this problem, as there are 2**99 altogether!
# If you could check one trillion (10**12) routes every second it would take
# over twenty billion years to check them all. There is an efficient
# algorithm to solve it. ;)

from python_code.decorators import euler_timer
from python_code.functions import get_data
from python_code.functions import max_sum

def main(verbose=False):
    triangle = get_data(67).strip()
    TRIANGLE_MAT = [[int(elt) for elt in line.split()]
                    for line in triangle.split("\n") if line]
    return max_sum(TRIANGLE_MAT)

if __name__ == '__main__':
    print euler_timer(67)(main)(verbose=True)
