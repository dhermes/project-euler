#!/usr/bin/env python

# There are ten composites below thirty containing precisely two, not
# necessarily distinct, prime factors:
# 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

# How many composite integers, n < 10**8, have precisely two, not necessarily
# distinct, prime factors?

from bisect import bisect
from math import sqrt

from python.decorators import euler_timer
from python.functions import sieve


def main(verbose=False):
    MAX_n = 10 ** 8
    # q <= p, q**2 <= pq = n < max_n, q < sqrt(max_n)
    # 2 <= q, 2p <= pq < max_n, p < max_n/2
    # Given q, pq < max_n, p < max_n/q
    PRIMES = sieve(MAX_n / 2)  # integer division intended
    result = 0
    q_max_index = bisect(PRIMES, sqrt(MAX_n))
    for q_index in range(q_max_index + 1):
        p_min_index = q_index
        p_max_index = bisect(PRIMES, MAX_n * 1.0 / PRIMES[q_index])
        result += p_max_index - p_min_index
    return result

if __name__ == '__main__':
    print euler_timer(187)(main)(verbose=True)
