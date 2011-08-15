#!/usr/bin/env python

# What is the largest prime factor of the number 600851475143

from python_code.decorators import euler_timer
from python_code.functions import prime_factors

def main(verbose=False):
    return max(prime_factors(600851475143))

if __name__ == "__main__":
    print euler_timer(3)(main)(verbose=True)
