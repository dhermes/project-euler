#!/usr/bin/env python

# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13

# This is the longest sum of consecutive primes that adds to a prime
# below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds
# to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the
# most consecutive primes?

from math import sqrt

from python.decorators import euler_timer
from python.functions import sieve


def max_prime_length(digits, primes=[]):
    """
    Returns the length of the longest string of primes
    (starting at 2,3,5,...) that will sum to less 10**digits
    """
    cap = 10 ** digits
    if primes == []:
        primes = sieve(int(4 * sqrt(cap)))
    count = 0
    num_primes = 0
    for prime in primes:
        if count + prime < cap:
            count += prime
            num_primes += 1
        else:
            return num_primes
    raise ValueError("max_prime_length failed logic.")


def all_prime_seqs(length, digits, primes=[]):
    """
    Returns all sequences of primes of

    Assumes length <= max_prime_length(digits)
    """
    cap = 10 ** digits
    if primes == []:
        primes = sieve(cap)

    result = []
    final_index = length - 1
    curr = primes[final_index - length + 1:final_index + 1]
    running_sum = sum(curr)
    while running_sum < cap:
        running_sum -= curr[0]  # remove the smallest value from the sum
        result.append(curr)
        final_index += 1
        curr = primes[final_index - length + 1:final_index + 1]
        running_sum += curr[-1]  # add the new largest
    return result


def prime_sequence_exists(length, digits, primes=[]):
    """
    Returns True if a sequence of length consecutive primes which sums
    to less than 10**digits also sums to a prime number
    """
    cap = 10 ** digits
    if primes == []:
        primes = sieve(cap)
    sums = [sum(seq) for seq in all_prime_seqs(length, digits, primes)]
    return (set(sums).intersection(primes) != set())


def longest_prime_sequence(digits, primes=[]):
    """
    Returns the length of the most consecutive primes which sum
    to a prime and sum to less then 10**digits
    """
    if primes == []:
        primes = sieve(10 ** digits)
    max_length = max_prime_length(digits, primes)
    for length in range(max_length, 0, -1):
        if prime_sequence_exists(length, digits, primes):
            return length
    raise ValueError("Algorithm failed")


def longest_prime(digits):
    primes = sieve(10 ** digits)
    length = longest_prime_sequence(digits, primes)
    sums = [sum(seq) for seq in all_prime_seqs(length, digits, primes)]
    return max(set(sums).intersection(primes))


def main(verbose=False):
    return longest_prime(6)

if __name__ == '__main__':
    print euler_timer(50)(main)(verbose=True)
