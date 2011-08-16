#!/usr/bin/env python

# We use a sieve type method to calculate
# the sum of all proper divisors up to n
# by looping through all possible factors
# and adding to the sum for each number
# that the factor divides into

from python_code.decorators import euler_timer

def proper_divisor_sums(n):
    result = [0]*(n + 1)
    # loop over all possible divisors
    for divisor in xrange(1, n + 1):
        # loop over all numbers that
        # i divides properly (we want
        # the sum of proper divisors)
        for parent in xrange(2*divisor, n + 1, divisor):
            result[parent] += divisor
    return result

def amicable_cycle(n, cycle_hash, divisors, break_point):
    if n in cycle_hash:
        return cycle_hash[n][1]

    cycle = [n]
    next = divisors[n]
    while (next not in cycle_hash and
           next not in cycle and
           next <= break_point):
        cycle.append(next)
        next = divisors[next]

    if next > break_point:
        set_val = [None]
    elif next in cycle_hash:
        set_val = cycle_hash[next][1]
    elif next in cycle:
        start = cycle.index(next)
        set_val = cycle[start:]
    else:
        raise Exception("Cycle should've occurred, check algorithm")
    for val in cycle:
        cycle_hash[val] = (divisors[val], set_val[:])
    return cycle_hash[n][1]

def main(verbose=False):
    MAX_n = 10**6
    divisors = proper_divisor_sums(MAX_n)
    chains = {1: (0, [0]),
              2: (1, [0]),
              3: (1, [0])}

    best_length = 1
    longest_chain = [0]
    for i in range(4, MAX_n + 1):
        chain = amicable_cycle(i, chains, divisors, MAX_n)
        if len(chain) > best_length:
            best_length = len(chain)
            longest_chain = chain[:]

    return min(longest_chain)

if __name__ == '__main__':
    print euler_timer(95)(main)(verbose=True)
