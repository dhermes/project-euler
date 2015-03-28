#!/usr/bin/env python

# Find the difference between the sum of the
# squares of the first one hundred natural
# numbers and the square of the sum.

from python.decorators import euler_timer
from python.functions import polygonal_number


def sum_first_n_sq(n):
    return n * (n + 1) * (2 * n + 1) / 6


def main(verbose=False):
    return abs(sum_first_n_sq(100) - polygonal_number(3, 100) ** 2)

if __name__ == '__main__':
    print euler_timer(6)(main)(verbose=True)
