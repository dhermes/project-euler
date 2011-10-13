#!/usr/bin/env python

from math import factorial

from python.decorators import euler_timer

def main(verbose=False):
    n = 50
    count = 0
    for red in range(2, n + 1, 2):
        black = n - red
        blocks = black + red/2
        count += factorial(blocks)/(factorial(black)*factorial(red/2))
    for green in range(3, n + 1, 3):
        black = n - green
        blocks = black + green/3
        count += factorial(blocks)/(factorial(black)*factorial(green/3))
    for blue in range(4, n + 1, 4):
        black = n - blue
        blocks = black + blue/4
        count += factorial(blocks)/(factorial(black)*factorial(blue/4))
    return count

if __name__ == '__main__':
    print euler_timer(116)(main)(verbose=True)
