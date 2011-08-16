#!/usr/bin/env python

import operator

from python_code.decorators import euler_timer
from python_code.functions import polygonal_number
from python_code.functions import reverse_polygonal_number

def all_polygonal(s, digits):
    result = []
    for i in range(10**digits):
        curr = polygonal_number(s, i)
        if curr >= 10**(digits - 1):
            if curr < 10**digits:
                result.append(curr)
            else:
                break

    return result

def possible_digits_key():
    left_digits = set()
    right_digits = set()

    four_digits = {}
    for sides in range(3, 9):
        four_digits[sides] = all_polygonal(sides, 4)
        left_digits.update([str(num)[:2] for num in four_digits[sides]])
        right_digits.update([str(num)[-2:] for num in four_digits[sides]])

    two_digit_candidates = left_digits.intersection(right_digits)

    result = {}
    for sides in range(3, 9):
        possible = [elt for elt in four_digits[sides]
                    if str(elt)[:2] in two_digit_candidates
                    and str(elt)[-2:] in two_digit_candidates]

        for number in possible:
            left = str(number)[:2]
            right = str(number)[-2:]
            if left in result:
                result[left].append((right, sides))
            else:
                result[left] = [(right, sides)]

    return result

def find_paths(start_val, start_sides, length, possible):
    """
    Starting from (XX, sides) we use the possible paths
    to move from one to the next, without repeating

    E.G. if start is ('95', 7) then we look in possible['95']
    and find [('91', 3), ('60', 5), ('17', 7)] so we will extend
    at that step to
    [[('95', 7), ('91', 3)], [('95', 7), ('60', 5)]]
    """
    paths = [[(start_val, start_sides)]]

    for i in range(length - 1):
        new_paths = []
        for path in paths:
            digits = [elt[0] for elt in path]
            sides = [elt[1] for elt in path]

            last_val = path[-1][0]
            # Extends each path by 1 to all the other
            # possible matches which don't conflict
            # with something already in path
            to_add = [path + [elt] for elt in possible[last_val]
                      if elt[0] not in digits
                      and elt[1] not in sides]
            new_paths.extend(to_add)

        paths = new_paths[:]

    return paths

def successful_path():
    """
    Returns the first set of 6 (XX, sides) pairs that form
    a path according to find_paths
    """
    possible = possible_digits_key()
    start_points = set(reduce(operator.add, possible.values()))

    for start_point in start_points:
        value, sides = start_point
        for path in find_paths(value, sides, 6, possible):
            # Once we establish the path, we need to
            # see if the cycle can be completed
            # So we check if the first element in the path
            # is a possible value for the last value in
            # the path
            last_val = path[-1][0]
            candidate = possible[last_val]
            if path[0] in candidate:
                return path
    raise ValueError("Algorithm on 61 failed.")

def main(verbose=False):
    COLORS = ['\033[98m',
              '\033[96m',
              '\033[95m',
              '\033[94m',
              '\033[92m',
              '\033[91m',
              '\033[98m'] # Loops back to beginning
    ENDC = '\033[0m'

    path = successful_path()
    result = [[path[i][0] + path[i + 1][0], path[i + 1][1]]
              for i in range(5)]
    result.append([path[-1][0] + path[0][0], path[0][1]])
    result = [elt + [reverse_polygonal_number(elt[1], int(elt[0]))]
              for elt in result]
    display = ""
    for i, entry in enumerate(result):
        value, sides, number = entry
        left = str(value)[:2]
        right = str(value)[-2:]
        colored_val = "".join([COLORS[i], left, ENDC,
                               COLORS[i+1], right, ENDC])
        display += "\nP_(%s,%s) = %s" % (sides, number, colored_val)
    if verbose:
        return "%s.%s" % (sum([int(match[0]) for match in result]), display)
    else:
        return sum([int(match[0]) for match in result])

if __name__ == '__main__':
    print euler_timer(61)(main)(verbose=True)
