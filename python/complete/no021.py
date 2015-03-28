#!/usr/bin/env python

from python.decorators import euler_timer
from python.functions import all_factors


def main(verbose=False):
    n = 10000
    factors = all_factors(n - 1)

    # sum of proper divisors
    first_pass = [sum(factors[i]) - i for i in range(1, n)]
    max_out = max(first_pass)

    factors = all_factors(max_out, factors)

    # applying sum of divisors twice to i we have
    # s_1 = func(i), s_2 = func(s_1)
    # s_1 = sum(factors[i]) - i, s_2 = sum(factors[s_1]) - s_1
    # i == s_2 <==>
    # i == sum(factors[sum(factors[i]) - i]) - (sum(factors[i]) - i) <==>
    # sum(factors[sum(factors[i]) - i]) == sum(factors[i])
    # Similarly s_1 != i <==> sum(factors[i]) != 2*i
    result = [i for i in range(2, n) if
              sum(factors[sum(factors[i]) - i]) == sum(factors[i]) and
              sum(factors[i]) != 2 * i]

    if verbose:
        return '%s.\nThe full list of such amicable numbers is %s.' % (
            sum(result), ', '.join(str(elt) for elt in result))
    else:
        return sum(result)

if __name__ == '__main__':
    print euler_timer(21)(main)(verbose=True)
