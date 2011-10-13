#!/usr/bin/env python

# What is the sum of the digits of the number 2^(1000)?

from python.decorators import euler_timer

def main(verbose=False):
    return sum([int(dig) for dig in str(2**1000)])

if __name__ == '__main__':
    print euler_timer(16)(main)(verbose=True)
