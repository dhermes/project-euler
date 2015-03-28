#!/usr/bin/env python

# A number n is called abundant if the sum of its proper divisors exceeds n.

# By mathematical analysis, it can be shown that all integers greater than
# 28123 can be written as the sum of two abundant numbers.

# Find the sum of all the positive integers which cannot be written as
# the sum of two abundant numbers.

import operator

from python.decorators import euler_timer
from python.functions import all_factors


def abundant_numbers(n):
    factor_hash = all_factors(n)
    # sum of proper divisors
    return [i for i in range(2, n + 1) if i < sum(factor_hash[i]) - i]


def main(verbose=False):
    abundants = abundant_numbers(28123)
    sums = [False] * (28123 + 1)

    length = len(abundants)
    for index in range(length):
        for second_index in range(index, length):
            val1 = abundants[index]
            val2 = abundants[second_index]
            if (val1 + val2 <= 28123):
                sums[val1 + val2] = True

    # those with indices set to false are the ones which can't be written
    # as the sum of two abundant numbers, so we sum them
    return sum(i for i, bool_val in enumerate(sums) if not bool_val)

if __name__ == '__main__':
    print euler_timer(23)(main)(verbose=True)
