#!/usr/bin/env python

# Find the value of d < 1000 for which ^(1)/_(d) contains the
# longest recurring cycle in its decimal fraction part.

from python.decorators import euler_timer
from python.functions import order_mod_n
from python.functions import robust_divide

def main(verbose=False):
    max_index = -1
    max_block_size = -1
    for i in range(1, 1000):
        stripped_val = robust_divide(robust_divide(i, 2), 5)
        if stripped_val == 1:
            block_size = 0
        else:
            block_size = order_mod_n(10, stripped_val)
        if block_size > max_block_size:
            max_block_size = block_size
            max_index = i

    return max_index

if __name__ == '__main__':
    print euler_timer(26)(main)(verbose=True)
