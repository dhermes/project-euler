#!/usr/bin/env python

# Find the sum of all the primes below two million.

from python_code.decorators import euler_timer
from python_code.functions import sieve

def main(verbose=False):
    return sum(sieve(2000000 - 1))

if __name__ == '__main__':
    print euler_timer(10)(main)(verbose=True)
