#!/usr/bin/env python

from python.decorators import euler_timer
from python.functions import prime_divides_repunit_power10
from python.functions import sieve

def main(verbose=False):
    PRIMES = sieve(10**5)
    running_sum = 0
    for prime in PRIMES:
        if not prime_divides_repunit_power10(prime):
            running_sum += prime
    return running_sum

if __name__ == '__main__':
    print euler_timer(133)(main)(verbose=True)
