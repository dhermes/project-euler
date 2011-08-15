#!/usr/bin/env python

# Find the greatest product of five consecutive
# digits in the 1000-digit number.

import operator

from python_code.decorators import euler_timer
from python_code.functions import get_data

def product_consec_digits(number, consecutive):
    """
    Returns the largest product of "consecutive"
    consecutive digits from number
    """
    digits = [int(dig) for dig in str(number)]
    max_start = len(digits) - consecutive
    return [reduce(operator.mul, digits[i:i + consecutive])
            for i in range(max_start + 1)]

def main(verbose=False):
    n = int("".join([line.strip() for line in get_data(8).split("\n")]))

    return max(product_consec_digits(n, 5))

if __name__ == "__main__":
    print euler_timer(8)(main)(verbose=True)
