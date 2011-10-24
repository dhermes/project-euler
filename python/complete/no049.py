#!/usr/bin/env python

# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
# increases by 3330, is unusual in two ways: (i) each of the three
# terms are prime, and, (ii) each of the 4-digit numbers are
# permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
# primes, exhibiting this property, but there is one other 4-digit
# increasing sequence.

# What 12-digit number do you form by concatenating the three terms
# in this sequence?

from python.decorators import euler_timer
from python.functions import all_subsets
from python.functions import sieve

def find_arithmetic(list_):
    if len(list_) < 3:
        raise ValueError("List wrong size.")

    candidates = all_subsets(list_, 3)
    for cand in candidates:
        if cand[0] + cand[2] == 2*cand[1]:
            return cand
    return []

def main(verbose=False):
    primes = [prime for prime in sieve(10000) if prime > 999]
    primes_by_digits = {}
    for prime in primes:
        key = "".join(sorted(digit for digit in str(prime)))
        # sets value to [] if not set, returns value at key
        primes_by_digits.setdefault(key, []).append(prime)

    result = []
    for key in primes_by_digits:
        candidate = primes_by_digits[key]
        if len(candidate) >= 3:
            soln = find_arithmetic(candidate)
            if soln:
                result.append("".join(str(num) for num in sorted(soln)))
    return result[0]

if __name__ == '__main__':
    print euler_timer(49)(main)(verbose=True)
