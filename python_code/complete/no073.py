#!/usr/bin/env python

# Consider the fraction, n/d, where n and d are positive integers.
# If n < d and HCF(n,d)=1, it is called a reduced proper fraction.

# If we list the set of reduced proper fractions for d <= 8 in
# ascending order of size, we get:
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2,
# 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

# It can be seen that there are 3 fractions between 1/3 and 1/2.

# How many fractions lie between 1/3 and 1/2 in the sorted set of
# reduced proper fractions for d <= 12,000?

# ALGO
# We simply seek 1/3 <= n/d <= 1/2 with (n, d) = 1
# This is equivalent to d/3 <= n <= d/2 or
# ceil(d/3) <= n <= floor(d/2)
# Note we'll never have conflicts since for d > 3,
# (n, d) = 1 implies n/d = 1/2 or n/d = 1/3 is
# impossible

from fractions import gcd
from math import ceil
from math import floor

from python_code.decorators import euler_timer

def main(verbose=False):
    MAX_d = 12000

    count = 0
    for d in range(4, MAX_d + 1):
        low = int(ceil(d/3.0))
        high = int(floor(d/2.0))
        for n in range(low, high + 1):
            if gcd(d, n) == 1:
                count += 1
    return count

if __name__ == "__main__":
    print euler_timer(73)(main)(verbose=True)
