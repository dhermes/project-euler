#!/usr/bin/env python

# What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?

from fractions import gcd

from python_code.decorators import euler_timer

def min_product(n):
    if n < 2:
        return 1

    prod = min_product(n - 1)
    shared = gcd(prod, n)
    return prod*n/shared

def main(verbose=False):
    return min_product(20)

if __name__ == '__main__':
    print euler_timer(5)(main)(verbose=True)
