#!/usr/bin/env python

# Find the last ten digits of the series 1^1 + 2^2 + 3^3 + ... + 1000^1000.

from python.decorators import euler_timer

def main(verbose=False):
    result = 0
    for i in range(1, 1000 + 1):
        result = (result + pow(i, i, 10**10)) % 10**10
    return result

if __name__ == '__main__':
    print euler_timer(48)(main)(verbose=True)
