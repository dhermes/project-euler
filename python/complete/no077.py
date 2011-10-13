#!/usr/bin/env python

# It is possible to write ten as the sum of primes in
# exactly five different ways:

# 7 + 3
# 5 + 5
# 5 + 3 + 2
# 3 + 3 + 2 + 2
# 2 + 2 + 2 + 2 + 2

# What is the first value which can be written as the sum of
# primes in over five thousand different ways?

#################################
# Let pp(k, n) represent the number of partitions of n
# using only primes at least as large as p_k (the kth prime)

# Since the primes are either all greater than p_k or one
# of them is equal we have
# pp(k, n) = pp(k+1, n) + pp(k, n - p_k)
# p_0 = 2, we want to compute pp(0, n) for all n and continue
# doing so until pp(0, n) > 5000

# Boundary
# p(k, n) = 0 if p_k > n
# p(k, n) = 1 if p_k = n
# pp(k, n) = pp(k+1, n) + pp(k, n - p_k)

############## EXAMPLE TABLE ##############
# n\k | 0 | 1 | 2 |
# -----------------
#  1  | 0 | 0 | 0 |
# -----------------
#  2  | 1 | 0 | 0 |
# -----------------
#  3  | 1 | 1 | 0 |
# -----------------
#  4  | 1 | 0 | 0 |
# -----------------
#  5  | 1 | 1 | 1 |
# -----------------

from python.decorators import euler_timer
from python.functions import sieve

def prime_partitions(n, primes):
    p = {}
    for k in range(1, n + 1):
        p[(k, k)] = 1
        for i in range(k - 1, 0, -1):
            if i > k - i:
                p[(i, k)] = p[(i + 1, k)]
            else:
                p[(i, k)] = p[(i + 1, k)] + p[(i, k - i)]
    return p[(1, n)]

def main(verbose=False):
    max_prime_val = 10**2
    PRIMES = sieve(max_prime_val)

    pp = {(0, 1): 0,
          (1, 1): 0,
          (2, 1): 0,
          (0, 2): 1,
          (1, 2): 0,
          (2, 2): 0}
    curr_val = -1
    n = 2
    curr_prime_index = 1
    while curr_val < 5000:
        n += 1
        if n > PRIMES[curr_prime_index]:
            curr_prime_index += 1
            if curr_prime_index >= len(PRIMES):
                raise ValueError("Primes is too small: %s" % curr_val)

        prime_index = curr_prime_index
        # First reduce the prime_index, "k" until the prime itself
        # does not exceed n
        while PRIMES[prime_index] > n:
            pp[(prime_index, n)] = 0
            prime_index -= 1
        # If n is a prime number, then after doing so, we know that
        # PRIMES[prime_index] == n, hence pp(p_i, n) = 1 and we
        # can reduce the index further
        if PRIMES[prime_index] == n:
            pp[(prime_index, n)] = 1
            prime_index -= 1

        for index in range(prime_index, -1, -1):
            prime_val = PRIMES[index]
            if prime_val > n - prime_val:
                pp[(index, n)] = pp[(index + 1, n)]
            else:
                pp[(index, n)] = pp[(index + 1, n)] + pp[(index, n - prime_val)]

        curr_val = pp[(0, n)]
    return n

if __name__ == '__main__':
    print euler_timer(77)(main)(verbose=True)
