#!/usr/bin/env python

from python.decorators import euler_timer
from python.functions import prime_divides_repunit_power10
from python.functions import sieve

def main(verbose=False):
    PRIMES = sieve(10**6)
    prime_index = 3 # p0=2, p1=3, and p2=5 are false positives
    matches = []
    while len(matches) < 40:
        prime = PRIMES[prime_index]
        if prime_divides_repunit_power10(prime, 9):
            matches.append(prime)
        prime_index += 1

    return sum(matches)

if __name__ == '__main__':
    print euler_timer(132)(main)(verbose=True)
