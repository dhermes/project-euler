#!/usr/bin/env python

# The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 X 7, 15 = 3 X 5

# The first three consecutive numbers to have three
# distinct prime factors are:
# 644 = 2^2 X 7 X 23, 645 = 3 X 5 X 43, 646 = 2 X 17 X 19

# Find the first four consecutive integers to have four distinct
# primes factors. What is the first of these numbers?

from python_code.decorators import euler_timer
from python_code.functions import prime_factors

def increment(value, list_):
    """
    This updates the value according to the list. Since we seek 4
    consecutive numbers with exactly 4 prime factors, we can jump
    4 numbers if the last doesn't have 4 factors, can jump 3 if
    the second to last doesn't have 4 factors, and so on
    """
    if list_[-1] != 4:
        return value + 4

    # We can assume the last element is a 4
    if list_[-2:] != [4, 4]:
        return value + 3

    # We can assume the last 2 elements are [4,4]
    if list_[-3:] != [4, 4, 4]:
        return value + 2

    # We can assume the last 3 elements are [4,4,4]
    return value + 1

def main(verbose=False):
    # Find the first four consecutive integers to have four distinct
    # primes factors. What is the first of these numbers?

    factor_hash = {1: [], 2: [2]}
    # Smallest product of 4 primes is 2*3*5*7 = 210
    # We need to update the hash to get to this point
    for i in range(3,210 + 1):
        prime_factors(i, hash_=factor_hash)

    smallest = 210 # The smallest integer of the four
    num_factors = [ len(prime_factors(smallest + i,
                                      unique=True,
                                      hash_=factor_hash))
                     for i in range(4) ]
    while num_factors != [4,4,4,4]:
        smallest = increment(smallest, num_factors)
        num_factors = [ len(prime_factors(smallest + i,
                                          unique=True,
                                          hash_=factor_hash))
                         for i in range(4) ]
    return smallest

if __name__ == "__main__":
    print euler_timer(47)(main)(verbose=True)
