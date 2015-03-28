#!/usr/bin/env python

# R(k) = (10^k - 1)/9
# So the smallest k such that R(k) == 0 mod n is related to the order
# or the element 10 in the multiplicative group of units

# if 3 does not divide n, then 3 (hence 9) is invertible, so
# R(k) == 0 iff 10^k - 1 == 0 iff 10^k == 1 mod n, giving
# us A(n) = order of 10 modulo n in those cases
# if 3 does divide n, then 9 is not invertible, so
# R(k) == 0 mod n iff 10^k - 1 == 0 mod (9n) giving
# us A(n) = order of 10 modulo (9n) in those cases

from python.decorators import euler_timer
from python.functions import order_mod_n
from python.functions import sieve


def main(verbose=False):
    prime_max = 10 ** 5
    PRIMES = sieve(prime_max)
    found = []
    n = 2
    while len(found) < 25:
        n += 1
        if n > prime_max:
            prime_max *= 10
            PRIMES = sieve(prime_max)

        if n % 2 == 0 or n % 5 == 0 or n in PRIMES:
            continue

        basis = n
        if n % 3 == 0:
            basis = 9 * n

        if (n - 1) % order_mod_n(10, basis) == 0:
            found.append(n)
    if verbose:
        return '%s.\nAs a check, the first five values are calculated to be ' \
               '%s, as stated.' % (sum(found),
                                   ', '.join(str(num) for num in found[:5]))
    else:
        return sum(found)

if __name__ == '__main__':
    print euler_timer(130)(main)(verbose=True)
