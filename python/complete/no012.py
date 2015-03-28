#!/usr/bin/env python

# What is the value of the first triangle number to have over
# five hundred divisors?

from python.decorators import euler_timer
from python.functions import prime_factors


def list_frequencies(list_):
    result = {}
    for element in list_:
        # if element is not in result, sets to 1 (default 0 returned by get)
        result[element] = result.get(element, 0) + 1
    return result.items()


def special_num_factors(a, b, hash_):
    factors = prime_factors(a, unique=False, hash_=hash_) + \
              prime_factors(b, unique=False, hash_=hash_)
    factors = list_frequencies(factors)

    prod = 1
    for factor in factors:
        prod *= factor[1] + 1
    return prod


def num_factors_nth_triangular(n, hash_):
    if n % 2 == 0:
        return special_num_factors(n / 2, n + 1, hash_)
    else:
        return special_num_factors(n, (n + 1) / 2, hash_)


def main(verbose=False):
    n = 1
    h = {}
    num_fac = num_factors_nth_triangular(n, h)
    while num_fac <= 500:
        n += 1
        num_fac = num_factors_nth_triangular(n, h)
    if verbose:
        return "%s.\nIt is the %sth triangular number and has %s divisors." % (
            (n * (n + 1)) / 2, n, num_fac)
    else:
        return (n * (n + 1)) / 2

if __name__ == '__main__':
    print euler_timer(12)(main)(verbose=True)
