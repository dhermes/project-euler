#!/usr/bin/env python

# f(1) = 1, f(2) = 2
# if n is odd, we must have first term equal
# to 1, hence f(n) = f((n - 1)/2)
# if n is even, we can either have 0 or 2 as
# the first term, leaving us
# f(n) = f(n/2) + f((n - 2)/2)

from python.decorators import euler_timer

def f(n, hash_=None):
    if hash_ is None:
        hash_ = {}

    if n in hash_:
        return hash_[n]
    if n in [1, 2]:
        hash_[n] = n
        return n
    if n % 2 == 0:
        result = f(n/2) + f(n/2 - 1)
    else:
        result = f((n - 1)/2)
    hash_[n] = result
    return result

def main(verbose=False):
    f_hash = {}
    return f(10**25, f_hash)

if __name__ == '__main__':
    print euler_timer(169)(main)(verbose=True)
