#!/usr/bin/env python

# A number n is called abundant if the sum of its proper divisors exceeds n.

# By mathematical analysis, it can be shown that all integers greater than
# 28123 can be written as the sum of two abundant numbers.

# Find the sum of all the positive integers which cannot be written as
# the sum of two abundant numbers.

import operator

from python_code.decorators import euler_timer
from python_code.functions import all_factors
from python_code.functions import apply_to_list

def abundant_numbers(n):
    factor_hash = all_factors(n)
    # sum of proper divisors
    return [i for i in range(2, n + 1) if i < sum(factor_hash[i]) - i]

def main(verbose=False):
    abundants = abundant_numbers(28123)
    sums = sorted(set(apply_to_list(operator.add, abundants)))
    bad_ones = [i for i in range(28123 + 1) if i not in sums]
    return sum(bad_ones)

if __name__ == "__main__":
    print euler_timer(23)(main)(verbose=True)
