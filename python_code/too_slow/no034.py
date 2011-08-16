#!/usr/bin/env python

# Find the sum of all numbers which are equal to the sum
# of the factorial of their digits.

# We know if n has d digits, then sum(n) <= d*9! = 362880d and n >= 10*(d-1)
# hence sum(n) = n implies 3628800d >= 10^d. We must have d <= 7.

from math import factorial

from python_code.decorators import euler_timer

def fact_sum_digs(n):
    return sum([factorial(int(dig)) for dig in str(n)])

def main(verbose=False):
    result = []
    for i in xrange(3, 9999999 + 1):
        if fact_sum_digs(i) == i:
            result.append(i)

    if verbose:
        return "%s.\nThe full list of numbers is as follows: %s." % (
            sum(result), ", ".join([str(number) for number in result]))
    else:
        return sum(result)

if __name__ == '__main__':
    print euler_timer(34)(main)(verbose=True)
