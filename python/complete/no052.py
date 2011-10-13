#!/usr/bin/env python

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x,
# and 6x, contain the same digits.

# NOTE:
# In order for x and 6x to have same digits, they must have same
# num of digits

# 10^(k - 1) <= x < 10^k has k digits
# Also need 10^(k - 1) <= 6x < 10^k
# Combining 10^(k - 1) <= x <= (10^k/6) <--- integer division

from python.decorators import euler_timer

def same_digs(n, multiplier):
    candidates = [n*mult for mult in range(1, multiplier + 1)]
    cand_digs = [sorted([int(dig) for dig in str(element)])
                 for element in candidates]
    # we sort the digits so only the content of the digit list matters
    return (cand_digs.count(cand_digs[0]) == len(cand_digs))

def find_sequence_same_digs(digs, multiplier):
    for n in range(10**(digs - 1), 10**digs/multiplier + 1):
        if same_digs(n, multiplier):
            return (True, n)
    return (False, -1)

def find_sequence_same(multiplier):
    digits = 1
    found = False

    while not found:
        found, val = find_sequence_same_digs(digits, multiplier)
        digits += 1
    return val

def main(verbose=False):
    return find_sequence_same(6)

if __name__ == '__main__':
    print euler_timer(52)(main)(verbose=True)
