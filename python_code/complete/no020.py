#!/usr/bin/env python

# Find the sum of the digits in the number 100!

from math import factorial

from python_code.decorators import euler_timer

def main(verbose=False):
    return sum([int(digit) for digit in str(factorial(100))])

if __name__ == '__main__':
    print euler_timer(20)(main)(verbose=True)
