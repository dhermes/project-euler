#!/usr/bin/env python

# We begin with a sorted list of values to choose from.
# If the value is not found, we log our biggest value and
# save the number of digits. We then start with 10**d
# and 2*(10**d), the next biggest values with only digits
# less than 3. We wish to find some x*(10**d) + y, where
# both x and y have only 1s and 2s and y has d digits
# or less. We want to x*(10**d) + y == 0 mod n

# Since we have all possible values y with d digits or less,
# we want to find the smallest match x such that
# x*(10**d) is in the set of residues (-y) % n

from itertools import product as i_product

from python.decorators import euler_timer

def find(n, value_list):
    for value in value_list:
        if value % n == 0:
            return value

    digs = len(str(max(value_list)))
    needed_residues = sorted(set([(-value) % n for value in value_list]))

    residue = (10**digs) % n
    actual_list = [1, 2]
    residue_form = [(residue*val) % n for val in actual_list]
    while set(residue_form).intersection(needed_residues) == set():
        next = []
        for val in actual_list:
            next.extend([10*val, 10*val + 1, 10*val + 2])
        actual_list = next
        residue_form = [(residue*val) % n for val in actual_list]

    best_match = min([val for val in actual_list
                      if (residue*val) % n in needed_residues])
    best_opposites = [val for val in value_list
                      if val % n == (-(best_match*residue)) % n]
    return (10**digs)*best_match + min(best_opposites)

def main(verbose=False):
    MAX_DIGITS = 12
    candidate_lists = [['0', '1', '2']]*MAX_DIGITS

    values = list(i_product(*candidate_lists))
    values = [int(''.join(value)) for value in values][1:]

    running_sum = 0
    for n in range(1, 10000 + 1):
        running_sum += find(n, values)/n
    return running_sum

if __name__ == '__main__':
    print euler_timer(303)(main)(verbose=True)
