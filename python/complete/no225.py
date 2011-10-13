#!/usr/bin/env python

from python.decorators import euler_timer
from python.functions import recurrence_next

def zero_absent(relation, initial_values, modulus):
    initial = [value % modulus for value in initial_values]
    curr = initial[:]

    if 0 in initial:
        return False

    curr = [value % modulus for value in recurrence_next(relation, curr)]
    while curr != initial:
        if 0 in curr:
            return False
        curr = [value % modulus for value in recurrence_next(relation, curr)]
    return True

def main(verbose=False):
    relation = [1,1,1]
    initial_values = [1,1,1]
    NUMBER_SUCCESSES = 124

    found = [27]
    modulus = 29
    while len(found) < NUMBER_SUCCESSES:
        if zero_absent(relation, initial_values, modulus):
            found.append(modulus)
        modulus += 2
    return found[NUMBER_SUCCESSES-1]

if __name__ == '__main__':
    print euler_timer(225)(main)(verbose=True)
