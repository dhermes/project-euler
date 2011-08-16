#!/usr/bin/env python

import operator

from python_code.decorators import euler_timer
from python_code.functions import all_permutations
from python_code.functions import get_data

def main(verbose=False):
    data = [[int(dig) for dig in row] for row
            in get_data(79).split("\r\n") if row]

    all_values = list(set(reduce(operator.add, data)))
    for password in all_permutations(all_values):
        correct = True
        for left, middle, right in data:
            left_index = password.index(left)
            middle_index = password.index(middle)
            right_index = password.index(right)
            if not (left_index < middle_index < right_index):
                correct = False
                break
        if correct:
            break
    if not correct:
        raise Exception("No match found")
    return ''.join([str(key) for key in password])

if __name__ == '__main__':
    print euler_timer(79)(main)(verbose=True)
