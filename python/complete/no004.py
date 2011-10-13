#!/usr/bin/env python

# Find the largest palindrome made from the
# product of two 3-digit numbers

# 100**2 = 10000 <= a*b <= 998001 = 999**2

import operator

from python.decorators import euler_timer
from python.functions import apply_to_list
from python.functions import is_palindrome

def main(verbose=False):
    products = apply_to_list(operator.mul, range(100,1000))
    return max([elt for elt in products if is_palindrome(elt)])

if __name__ == '__main__':
    print euler_timer(4)(main)(verbose=True)

