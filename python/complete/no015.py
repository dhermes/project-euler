#!/usr/bin/env python

# Starting in the top left corner of a 2 x 2 grid, there are
# 6 routes (without backtracking) to the bottom right corner.
# How many routes are there through a 20 x 20 grid?

from python.decorators import euler_timer
from python.functions import choose


def main(verbose=False):
    # In an n x m grid there are (n + m) C m = (n + m) C n such paths.
    return choose(20 + 20, 20)

if __name__ == '__main__':
    print euler_timer(15)(main)(verbose=True)
