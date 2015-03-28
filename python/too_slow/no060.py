#!/usr/bin/env python

from python.decorators import euler_timer
from python.functions import is_prime
from python.functions import sieve


def prime_concat_partners(list_, primes, failure_point):
    result = {}

    length = len(list_)
    for first in range(length - 1):
        n1 = list_[first]
        for second in range(first + 1, length):
            n2 = list_[second]
            cand1 = int(str(n1) + str(n2))
            cand2 = int(str(n2) + str(n1))
            if is_prime(cand1, primes=primes, failure_point=failure_point):
                if is_prime(cand2, primes=primes, failure_point=failure_point):
                    # sets value to [] if not set, returns value at key
                    result.setdefault(n1, []).append(n2)
                    result.setdefault(n2, []).append(n1)
    return result


def possible_pairings(partner_hash, length):
    # length = 1
    result = [[key] for key in partner_hash]
    for size in range(2, length + 1):
        next_iteration = []
        for subset in result:
            possible_additions = partner_hash[subset[0]]
            for val in subset:
                possible_additions = [entry for entry in possible_additions
                                      if entry in partner_hash[val]]
            next_iteration.extend([subset[:] + [candidate]
                                   for candidate in possible_additions])
        result = next_iteration
    return result


def main(verbose=False):
    MAX_n = 10 ** 4
    PRIMES = sieve(MAX_n)
    partner_hash = prime_concat_partners(PRIMES, PRIMES, MAX_n ** 2)
    valid = possible_pairings(partner_hash, 5)

    min_sum = 10 ** 10
    min_set = None
    for subset in valid:
        if sum(subset) < min_sum:
            min_sum = sum(subset)
            min_set = subset

    min_set = [str(prime) for prime in sorted(min_set)]
    if verbose:
        return '%s.\nThis is obtained with the primes %s.' % (
            min_sum, ', '.join(min_set))
    else:
        return min_sum

if __name__ == '__main__':
    print euler_timer(60)(main)(verbose=True)
