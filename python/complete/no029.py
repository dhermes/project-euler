#!/usr/bin/env python

import operator

from python.decorators import euler_timer
from python.functions import apply_to_list


def main(verbose=False):
    n = 100
    powers = apply_to_list(operator.pow, range(2, n + 1))
    return len(set(powers))

if __name__ == '__main__':
    print euler_timer(29)(main)(verbose=True)
