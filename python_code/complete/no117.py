#!/usr/bin/env python

import operator

from math import factorial

from python_code.decorators import euler_timer

def main(verbose=False):
    n = 50
    count = 0
    for red in range(0, n + 1, 2):
        for green in range(0, n + 1 - red, 3):
            for blue in range(0, n + 1 - red - green, 4):
                black = n - red - green - blue
                blocks = black + red/2 + green/3 + blue/4
                denominator = reduce(operator.mul, [factorial(black),
                                                    factorial(red/2),
                                                    factorial(green/3),
                                                    factorial(blue/4)])
                count += factorial(blocks)/denominator
    return count

if __name__ == '__main__':
    print euler_timer(117)(main)(verbose=True)
