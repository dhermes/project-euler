#!/usr/bin/env python

from math import log

from python.decorators import euler_timer
from python.functions import sieve

def hamming_type(max_n, primes):
    # assumes primes is sorted
    if primes == []:
        return 1

    count = 0
    prime = primes[0]
    max_power = int(log(max_n)/log(prime))
    for power in range(max_power + 1):
        # each prime can contribute as few as zero
        # and as many as max_power factors
        # by removing prime from the list, we count
        # all such numbers with exactly power factors
        # of prime
        count += hamming_type(max_n/(prime**power), primes[1:])
    return count

def main(verbose=False):
    PRIMES = sieve(100)
    return hamming_type(10**9, PRIMES)

if __name__ == '__main__':
    print euler_timer(204)(main)(verbose=True)

