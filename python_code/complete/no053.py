#!/usr/bin/env python

# How many, not necessarily distinct, values of  n_C_r, for 1 <= n <= 100,
# are greater than one-million?

# Witness
# 1 3 3 1
# When n is odd, the maximum occurs at r = (n - 1)/2 and (n + 1)/2
# When n is odd there are (n + 1)/2 values that occur twice
# 1 4 6 4 1
# When n is even, the maximum occurs at r = n/2
# When n is even there are (n - 1)/2 values that occur twice, and
# one that occurs once

# In either case we go up to n/2 (integer division) and then add on the
# next integer, in the odd case, it is double, in the even case only single

# n_C_r --> n_C_(r + 1), n!/(r!(n-r-1)!(n-r)) --> n!/((r+1) r!(n-r-1)!)

from python_code.decorators import euler_timer

def num_over_limit(n, limit):
    """
    Returns the number of values for n C r that are greater than limit
    """
    if n == 1:
        if 1 > limit:
            return 2
        else:
            return 0

    prod = 1
    for r in range(n/2 - 1):
        if prod > limit:
            return (n/2 - r)*2 + (n % 2) + 1
        prod = prod * (n - r) / (r + 1)
    if prod > limit:
        return 2 + (n % 2) + 1
    prod = prod * (n - n/2 + 1) / (n/2)
    if prod > limit:
        return (n % 2) + 1
    return 0

def all_over_limit(n_max, limit):
    """
    Returns the number of values for n C r that are greater than limit
    as n goes from 1 up to n_max
    """
    return sum([num_over_limit(n, limit) for n in range(1, n_max + 1)])

def main(verbose=False):
    return all_over_limit(100, 10**6)

if __name__ == '__main__':
    print euler_timer(53)(main)(verbose=True)
