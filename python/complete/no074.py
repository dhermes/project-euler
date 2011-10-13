#!/usr/bin/env python

# Perhaps less well known is 169, in that it produces the longest chain of
# numbers that link back to 169; it turns out that there are only three
# such loops that exist:
#    169 --> 363601 --> 1454 --> 169
#    871 --> 45361 --> 871
#    872 --> 45362 --> 872
# It is not difficult to prove that EVERY starting number will eventually
# get stuck in a loop. For example,
#    69 --> 363600 --> 1454 --> 169 --> 363601 (--> 1454)
#    78 --> 45360 --> 871 --> 45361 (--> 871)
#    540 --> 145 (--> 145)

# Starting with 69 produces a chain of five non-repeating terms, but the
# longest non-repeating chain with a starting number below one million is
# sixty terms. How many chains, with a starting number below one million,
# contain exactly sixty non-repeating terms?

from math import factorial

from python.decorators import euler_timer

def digit_factorial_sum(n, hash_={}):
    if n in hash_:
        return hash_[n]
    result = sum([factorial(int(dig)) for dig in str(n)])
    hash_[n] = result
    return result

def chain(n, next_hash={}, chain_hash={}):
    path = [n]
    if n in chain_hash:
        return chain_hash[n]
    next_ = digit_factorial_sum(path[-1], next_hash)
    while next_ not in path:
        if next_ in chain_hash:
            chain_hash[n] = path + chain_hash[next_]
            return chain_hash[n]
        path += [next_]
        next_ = digit_factorial_sum(path[-1], next_hash)
    chain_hash[n] = path
    return path

def main(verbose=False):
    chains = {}
    next_hash = {}
    for n in range(1, 10**6):
        chain(n, next_hash, chains)
        # This sets the value in chains
    return len([n for n in range(1, 10**6) if len(chains[n]) == 60])

if __name__ == '__main__':
    print euler_timer(74)(main)(verbose=True)
