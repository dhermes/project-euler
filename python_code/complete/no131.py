#!/usr/bin/env python

# We have (n**2)*(n + p) = m**3, we first show p does not divide n or m
# If p | m, then n != 0 mod p, implies LHS != 0, RAA ==> p | n
# But p | n means n = kp, (k**2)*(p**2)*p*(k + 1) = m**3
# hence k**3 + k**2 = (m/p)**3, but
# k**3 < k**3 + k**2 < k**3 + 3*(k**2) + 3*k + 1 = (k + 1)**3
# so this is impossible

# With this, let a prime q divide m**3 (hence m)
# We know q | n**2 or q | (n + p) or both since Z_q is a domain
# But q | n**2 ==> n == 0 mod q ==> n + p == p != 0 mod q;
# since by the above q | m, means q != p
# Thus all factors of q must divide n**2. Since q | m**3 and q
# prime we must have q**(3*k) | m**3 for some value of k,
# forcing q**(3*k) | n**2.
# Similarly, q | n + p ==> n == -p != 0 mod q, and the same argument
# implies q**(3*k) | n + p.
# This n + p must be composed of cubic prime powers dividing m**3,
# and similarly for n**2. Since (2, 3) = 1, this forces n to be a cube
# and makes p = (n + p) - n a difference of cubes

# Since p = r**3 - s**3 = (r - s)*(r**2 + r*s + s**2)
# p | r - s, implies r - s = 1 or p, but r - s = p, clearly won't work
# hence r = s + 1
# Given a problem max M, we just go up to the biggest L such that
# (L + 1)**3 - L**3 <= M, forcing 6*L + 3 <= sqrt(12*M - 3)

from math import sqrt

from python_code.decorators import euler_timer
from python_code.functions import sieve

def main(verbose=False):
    problem_max = 10**6
    count = 0
    PRIMES = sieve(problem_max)
    max_L = int(round((sqrt(12*problem_max - 3) - 3)/6))
    for L in xrange(1, max_L + 1):
        difference = (L + 1)**3 - L**3
        if difference in PRIMES:
            count += 1
    return count

if __name__ == "__main__":
    print euler_timer(131)(main)(verbose=True)

