#!/usr/bin/env python

# Find the value of n <= 1,000,000 for which n/PHI(n) is a maximum.
# n/PHI(n) = prod_(p | n) p/(p-1)

from python.decorators import euler_timer
from python.functions import sieve

def main(verbose=False):
    problem_max = 10**6
    PRIMES = sieve(problem_max)
    # ignore zero index
    ratios = [(1, index) for index in range(problem_max + 1)]
    for prime in PRIMES:
        ratios[prime::prime] = [((ratio*prime*1.0)/(prime - 1), index)
                                for ratio, index in ratios[prime::prime]]
    ratios.sort(key=lambda pair: pair[0], reverse=True)
    return ratios[0][1]

if __name__ == '__main__':
    print euler_timer(69)(main)(verbose=True)
