#!/usr/bin/env python

# Considering natural numbers of the form, a^(b), where a, b < 100, what
# is the maximum digital sum?

import operator

from python.decorators import euler_timer
from python.functions import apply_to_list

def digit_sum(n):
    return sum(int(dig) for dig in str(n))

def main(verbose=False):
    return max(digit_sum(val)
               for val in apply_to_list(operator.pow, range(1,100)))

if __name__ == '__main__':
    print euler_timer(56)(main)(verbose=True)
