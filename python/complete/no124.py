#!/usr/bin/env python

# The radical of n, rad(n), is the product of distinct prime factors of n.
# rad(12) = 2*3, rad(343) = 7

# If we calculate rad(n) for 1 <= n <= M, then sort them on rad(n), and
# sorting on n if the radical values are equal, we get a sequence
# E(k) for 1 <= k <= N

#  n  r  E
#  1  1  1
#  2  2  2
#  4  2  3
#  8  2  4
#  3  3  5
#  9  3  6
#  5  5  7
#  6  6  8
#  7  7  9
# 10 10 10

# Given this sequence E when M = 10**5,
# find E(10**4)

from python.decorators import euler_timer
from python.functions import first_prime_divisor
from python.functions import sieve

def all_radicals(n):
    PRIMES = sieve(n)
    result = {1: 1}
    for i in range(2, n + 1):
        if i in PRIMES:
            result[i] = i
        prime, quotient = first_prime_divisor(i, PRIMES)
        if quotient % prime == 0:
            result[i] = result[quotient]
        else:
            result[i] = result[quotient]*prime
    return result

def sorted_radicals(n):
    rad_dict = all_radicals(n)
    rad_vals = {}
    # since we go in order, we have
    # no need to sort within each radical value
    for i in range(1, n + 1):
        value = rad_dict[i]
        # sets value to [] if not set, returns value at key
        rad_vals.setdefault(value, []).append(i)

    result = []
    for value in sorted(rad_vals):
        result.extend(rad_vals[value])

    return result

def main(verbose=False):
    MAX_n = 10**5
    index = 10**4
    return sorted_radicals(MAX_n)[index - 1]

if __name__ == '__main__':
    print euler_timer(124)(main)(verbose=True)
