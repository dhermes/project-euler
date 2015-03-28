#!/usr/bin/env python

from python.decorators import euler_timer
from python.functions import fill_count


def main(verbose=False):
    count = 2
    n = 50
    while count <= 10 ** 6:
        n += 1
        count = fill_count(50, n)
    return n

if __name__ == '__main__':
    print euler_timer(115)(main)(verbose=True)
