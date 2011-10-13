#!/usr/bin/env python

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as
# the concatenated product of an integer with (1,2, ... , n) where n > 1?

from python.decorators import euler_timer

def is_pandigital_9(str_):
    for dig in [str(elt) for elt in range(1, 10)]:
        if str_.count(dig) != 1:
            return False
    return True

def all_pandigitals_1_to_n(n):
    to_mult = range(1, n + 1)
    multiplier = 1
    result = []

    curr = "".join([str(multiplier*elt) for elt in to_mult])
    while len(curr) < 10:
        if is_pandigital_9(curr):
            result.append(curr)
        multiplier += 1
        curr = "".join([str(multiplier*elt) for elt in to_mult])

    return result

def main(verbose=False):
    result = []
    for n in range(2, 10):
        result.extend(all_pandigitals_1_to_n(n))
    return max([int(elt) for elt in result])

if __name__ == '__main__':
    print euler_timer(38)(main)(verbose=True)
