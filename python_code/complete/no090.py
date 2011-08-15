#!/usr/bin/env python

from python_code.decorators import euler_timer
from python_code.functions import all_subsets

def can_concat(left, right, candidates):
    possible = ['%s%s' % (dig_l, dig_r) for dig_l in left for dig_r in right]
    for dig_l in right:
        for dig_r in left:
            possible.append('%s%s' % (dig_l, dig_r))
    return (len(set(possible).intersection(candidates)) == 9)

def main(verbose=False):
    dice = all_subsets(range(10), 6)
    size = len(dice)
    for i in range(size):
        if 6 in dice[i] and 9 not in dice[i]:
                dice[i].append(9)
        if 9 in dice[i] and 6 not in dice[i]:
                dice[i].append(6)

    count = 0
    candidates = [str(n**2).zfill(2) for n in range(1, 10)]
    for left_ind in range(size - 1):
        for right_ind in range(left_ind, size):
            if can_concat(dice[left_ind], dice[right_ind], candidates):
                count += 1
    return count

if __name__ == "__main__":
    print euler_timer(90)(main)(verbose=True)
