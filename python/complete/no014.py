#!/usr/bin/env python

# Which starting number, under one million, produces the
# longest chain? (Of the collatz chain)

from python.decorators import euler_timer

def collatz_next(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n + 1

def length(n, hash_):
    if n in hash_:
        return hash_[n]
    else:
        curr_length = 1 + length(collatz_next(n), hash_)
        hash_[n] = curr_length
        return curr_length

def max_collatz_length_up_to_n(n, hash_ = {1: 1}):
    max_length = -1
    max_length_at = -1
    for i in range(1, n + 1):
        if length(i, hash_) > max_length:
            max_length = length(i, hash_)
            max_length_at = i
    return [max_length_at , max_length]

def main(verbose=False):
    ans = max_collatz_length_up_to_n(999999)
    if verbose:
        return '%s.\nThe Collatz chain at %s has length %s.' % (
            ans[0], ans[0], ans[1])
    else:
        return ans[0]

if __name__ == '__main__':
    print euler_timer(14)(main)(verbose=True)
