#!/usr/bin/env python

# The cube, 41063625 (345**3), can be permuted to produce two other cubes:
# 56623104 (384**3) and 66430125 (405**3). In fact, 41063625 is the smallest
# cube which has exactly three permutations of its digits which are also cube.

# Find the smallest cube for which exactly five permutations
# of its digits are cube.

from python.decorators import euler_timer


def all_cubes(digits):
    # 10**(d-1) <= X**3 < 10**d
    cube_10 = 10 ** (1 / 3.0)
    M = int(cube_10 ** digits)
    if digits % 3 == 0:
        M = M - 1
    m = cube_10 ** (digits - 1)
    if abs(int(m) - m) < 0.01:
        m = int(m)
    else:
        m = int(m) + 1
    return [x ** 3 for x in range(m, M + 1)]


def has_k_perms(digits, k, cubes):
    sorted_cubes = {}
    for cube in cubes:
        sorted_digs = ''.join(sorted(str(cube)))
        # sets value to [] if not set, returns value at key
        sorted_cubes.setdefault(sorted_digs, []).append(cube)

    possible_matches = [value for value in sorted_cubes.values()
                        if len(value) == 5]

    possible_matches.sort(key=lambda list_: min(list_))
    if possible_matches:
        return min(possible_matches[0])
    else:
        return -1


def main(verbose=False):
    digits = len(str(41063625))
    cubes = all_cubes(digits)
    while has_k_perms(digits, 5, cubes) == -1:
        digits += 1
        cubes = all_cubes(digits)
    return has_k_perms(digits, 5, cubes)

if __name__ == '__main__':
    print euler_timer(62)(main)(verbose=True)
