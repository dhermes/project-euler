#!/usr/bin/env python

# We shall say that an n-digit number is pandigital if it makes use of all
# the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
# and is also prime.

# What is the largest n-digit pandigital prime that exists?

from math import sqrt

from python.decorators import euler_timer
from python.functions import all_permutations_digits
from python.functions import is_prime
from python.functions import sieve


def main(verbose=False):
    MAX_n = 987654321
    PRIMES = sieve(int(sqrt(MAX_n)))
    # A 9 digit pandigital will have digit sum 45, so can't be prime
    # must be divisible by 9
    for i in range(8, 1, -1):
        cand = [str(dig) for dig in range(1, i + 1)]
        cand = int("".join(cand))
        candidates = sorted(all_permutations_digits(cand))[::-1]
        for candidate in candidates:
            if is_prime(candidate, primes=PRIMES, failure_point=MAX_n):
                return candidate
    raise ValueError("No prime was found, algorithm busted.")

if __name__ == '__main__':
    print euler_timer(41)(main)(verbose=True)
