#!/usr/bin/env python

from python.decorators import euler_timer


def special_perms(num_2, num_3):
    if num_3 == 0:
        return [[2] * num_2]
    elif num_2 == 0:
        return [[3] * num_3]

    result = [[2] + perm for perm in special_perms(num_2 - 1, num_3)] + \
             [[3] + perm for perm in special_perms(num_2, num_3 - 1)]
    return result


def cumulative_sum(list_):
    result = [list_[0]]
    for entry in list_[1:]:
        result.append(result[-1] + entry)
    return result

# 2*x + 3*y = 32
# implies y = 2*y_star, x = 16 - 3*y_star for 0 <= y_star <= 5

def main(verbose=False):
    break_rows = []
    for y_star in range(5 + 1):
        x = 16 - 3 * y_star
        y = 2 * y_star
        for perm in special_perms(x, y):
            to_add = cumulative_sum(perm)
            if to_add[-1] != 32:
                raise ValueError("Unexpected output from cumulative_sum")
            break_rows.append(to_add[:-1])

    acceptable_next = {}
    for i, row in enumerate(break_rows):
        to_add = []
        for j, onto_row in enumerate(break_rows):
            # No matching breakpoints
            if set(row).intersection(onto_row) == set():
                to_add.append(j)
        acceptable_next[i] = to_add

    # for each key, this will list the number of acceptable
    # walls that end with the given key. Hence only 1
    # wall of height 1 ends with each key
    num_blocks_ending = {}
    for key in acceptable_next:
        num_blocks_ending[key] = {1: 1}

    blocks = 1
    while blocks < 10:
        blocks += 1
        for key, value in acceptable_next.items():
            for onto in value:
                to_add = num_blocks_ending[key][blocks - 1]
                # if blocks is not in num_blocks_ending[onto], sets to to_add
                # (default 0 returned by get)
                num_blocks_ending[onto][blocks] = \
                    num_blocks_ending[onto].get(blocks, 0) + to_add

    # we finally add together all walls of height 10 ending
    # with any key (so we loop over all keys)
    result = 0
    for key in num_blocks_ending:
        result += num_blocks_ending[key][10]
    return result

if __name__ == '__main__':
    print euler_timer(215)(main)(verbose=True)
