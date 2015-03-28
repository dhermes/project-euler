#!/usr/bin/env python

# The number 3797 has an interesting property. Being prime itself,
# it is possible to continuously remove digits from left to right,
# and remain prime at each stage:
# 3797, 797, 97, and 7.

# Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from
# left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import copy

from python.decorators import euler_timer
from python.functions import is_prime
from python.functions import sieve

def truncated_list(n, from_left):
    if from_left:
        digs = [dig for dig in str(n)]
        return [int("".join(digs[i:])) for i in range(len(digs))]
    # If the bool from_left is false, we are right
    else:
        digs = [dig for dig in str(n)]
        return [int("".join(digs[:i + 1])) for i in range(len(digs))]

def truncated_all(n):
    return list(set(truncated_list(n, True) + truncated_list(n, False)))

def is_truncatable_prime(n, primes):
    candidates = truncated_all(n)
    for candidate in candidates:
        if candidate in primes:
            continue
        elif is_prime(candidate):
            primes.add(candidate)
        else:
            return False
    return True

def find_first_n_truncatable(n, max_n):
    result = []
    primes = set(sieve(max_n)[4:]) # We don't include 2, 3, 5, or 7
    for prime in copy.copy(primes):
        if is_truncatable_prime(prime, primes):
            result.append(prime)
        if len(result) == n:
            return result

    if len(result) < n:
        raise Exception("Not enough found, raise max_n")

    return result

def main(verbose=False):
    ans = find_first_n_truncatable(11, 10**6)

    if verbose:
        return "%s.\nThe primes are: %s." % (
            sum(ans), ", ".join(str(prime) for prime in ans))
    else:
        return sum(ans)

if __name__ == '__main__':
    print euler_timer(37)(main)(verbose=True)
