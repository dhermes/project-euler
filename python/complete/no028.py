#!/usr/bin/env python

# Starting with the number 1 and moving to the right in a clockwise
# direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# What is the sum of the numbers on the diagonals in a 1001 by 1001
# spiral formed in the same way?

from python.decorators import euler_timer

# 1, 1, 2, 2, 3, 3, 4, 4, etc., every 2 is a corner

def spiral_sum(n):
    if n % 2 == 0:
        raise ValueError("Spiral only occurs on odds.")

    curr_val = 1
    total = 0

    # as we move along the corners on the spiral, the number of
    # steps (i.e. number of corners) dictates the size of each
    # new step. In almost all cases, the step increases by one
    # but every four, when the next corner wraps a new layer,
    # it does not increase
    step_num = 0
    step_size = 0
    while curr_val <= n ** 2:
        if step_num % 2 == 0:
            step_size += 1
        curr_val += step_size
        if step_num % 4 == 0:
            total += curr_val - 1
        else:
            total += curr_val
        step_num += 1

    return total


def main(verbose=False):
    return spiral_sum(1001)

if __name__ == '__main__':
    print euler_timer(28)(main)(verbose=True)
