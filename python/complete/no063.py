#!/usr/bin/env python

# The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit
# number, 134217728=8**9, is a ninth power.

# How many n-digit positive integers exist which are also an nth power?

#######################################################
# 10**(n - 1) <= N < 10**n have n digits
# So if N = k**n for some k we have
# 10**(1 - 1/n) <= k < 10, for k integer
# if 9 < 10**(1 - 1/n), there are no such k
# This occurs when ln(9) < (1 - 1/n)ln(10)
# 1/(1 - ln(9)/ln(10)) < n

from math import ceil
from math import log

from python.decorators import euler_timer

def num_n_digits(n):
    # 10**(1 - 1/n) <= k < 10, for k integer
    return 10 - int(ceil(10**(1 - 1.0/n)))

def main(verbose=False):
    MAX_n = int((1 - log(9)/log(10))**(-1))
    return sum([num_n_digits(i) for i in range(1, MAX_n + 1)])

if __name__ == '__main__':
    print euler_timer(63)(main)(verbose=True)
