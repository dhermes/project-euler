#!/usr/bin/env python

# What is the 10001st prime number?

from python.decorators import euler_timer
from python.functions import sieve


def main(verbose=False):
    # By the prime number theorem, pi(x) =~ x/ln(x)
    # pi(x) >= 10001 when x >= 10001 ln(x)
    # To be safe, we'll double it and solve
    # x = 20002 ln(x)

    # We are left with approximately 248490
    primes = sieve(248490)
    return primes[10001 - 1]

if __name__ == '__main__':
    print euler_timer(7)(main)(verbose=True)
