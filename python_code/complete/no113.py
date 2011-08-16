#!/usr/bin/env python

# Increasing number:
# For up to n digits, each number can be
# a_1...a_n
# d_1 = a_1, d_2 = a_2 - a_1, etc. where
# d_1 + d_2 + ... + d_j = a_j <= 9
# We need to allow the sum to be less than 9,
# so we have some other B such that
# d_1 + d_2 + ... + d_n + B = 9, then
# we have (n + 1) bins for 9 objects. To
# organize n dividers and 9 objects, we need
# a total of (n + 9 C 9) increasing sequences
# We must subtract 1 since 0,0,...,0 is allowed here

# Decreasing number:
# We consider each length separately, for a
# number of length L, we have
# a_L...a_1
# similarly we have d_1 = a_1, d_2 = a_2 - a_1, etc.
# And there are (L + 9 C 9) - 1 that are valid
# (the all zero again does not produce a number)
# Using the identity (k C k) + ... (n C k) = ((n + 1) C (k + 1))
# and the fact that (a C k) = 0 for a < k, summing
# over L = 1 to n, we have
# (n + 10 C 10) - n that are valid

# For each number of digits, the number k*(11...1) for
# 1 <= k <= 9 is both incr. and decr., so we have
# overcounted 9*n numbers

# Also, the length 1 case a_1 = 0 is overcounted

# All together we have
# (n + 10 C 10) - n + [(n + 9 C 9) - 1] - 9*n - 1

from python_code.decorators import euler_timer
from python_code.functions import choose

def main(verbose=False):
    n = 100
    return choose(n + 10, 10) + choose(n + 9, 9) - 10*n - 2

if __name__ == '__main__':
    print euler_timer(113)(main)(verbose=True)
