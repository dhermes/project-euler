#!/usr/bin/env python

# Find the value of n, 1 < n < 10**7, for which PHI(n) is a permutation of n
# and the ratio n/PHI(n) produces a minimum.

from python.decorators import euler_timer
from python.functions import sieve


def same_digits(n, m):
    dig_n = [dig for dig in str(n)]
    dig_m = [dig for dig in str(m)]
    return (sorted(dig_n) == sorted(dig_m))


def matches(problem_max):
    PRIMES = sieve(problem_max)
    phi_list = range(problem_max + 1)  # ignore zero index
    for prime in PRIMES:
        phi_list[prime::prime] = [(val / prime) * (prime - 1) for val in
                                  phi_list[prime::prime]]
    cands = [(val, phi_list[val]) for val in range(2, problem_max + 1)
             if same_digits(val, phi_list[val])]
    cands.sort(key=lambda cand: (cand[0] * 1.0) / cand[1])
    return cands[0][0]


def main(verbose=False):
    problem_max = 10 ** 7
    return matches(problem_max)

if __name__ == '__main__':
    print euler_timer(70)(main)(verbose=True)
