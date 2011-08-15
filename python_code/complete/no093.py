#!/usr/bin/env python

import operator

from python_code.decorators import euler_timer
from python_code.functions import all_permutations
from python_code.functions import all_subsets

# a D b D c D d, for D in {+,-,*,/}
# = {operator.add, operator.sub, operator.mul, operator.div}

# ALL POSSIBLE PARENTHESIS PLACEMENTS
# (a b) c d
# a b (c d)
# (a b) (c d)
# (a b c) d
# ((a b) c) d
# (a (b c)) d
# a (b c d)
# a ((b c) d)
# a (b (c d))

def do_operations_no_paren(operators, numbers):
    if len(operators) + 1 != len(numbers):
        raise Exception("MISDEED")

    if len(numbers) == 1:
        return numbers[0]


    for i, op in enumerate(operators):
        if op in [operator.mul, operator.div]:
            new_number = op(numbers[i], numbers[i+1])
            new_numbers = numbers[:i] + [new_number] + numbers[i+2:]
            new_operators = operators[:i] + operators[i+1:]
            return do_operations_no_paren(new_operators, new_numbers)

    # no mul or div found
    new_number = op(numbers[0], numbers[1])
    new_numbers = [new_number] + numbers[2:]
    new_operators = operators[1:]
    return do_operations_no_paren(new_operators, new_numbers)

def results(signs, numbers):
    # parentheses first
    # multiply or divide before add or subtract
    # left to right after all
    a, b, c, d = numbers
    s1, s2, s3 = signs

    result = []
    try:
        val = do_operations_no_paren([s2, s3], [s1(a, b), c, d])
        result.append(val)
    except ZeroDivisionError:
        pass
    try:
        val = do_operations_no_paren([s1, s2], [a, b, s3(c, d)])
        result.append(val)
    except ZeroDivisionError:
        pass
    try:
        val = do_operations_no_paren([s2], [s1(a, b), s3(c, d)])
        result.append(val)
    except ZeroDivisionError:
        pass
    try:
        val = do_operations_no_paren([s3],
            [do_operations_no_paren([s1, s2], [a, b, c]), d])
        result.append(val)
    except ZeroDivisionError:
        pass
    try:
        val = do_operations_no_paren([s3], [s2(s1(a, b), c), d])
        result.append(val)
    except ZeroDivisionError:
        pass
    try:
        val = do_operations_no_paren([s3], [s1(a, s2(b, c)), d])
        result.append(val)
    except ZeroDivisionError:
        pass
    try:
        val = do_operations_no_paren([s1],
            [a, do_operations_no_paren([s2, s3], [b, c, d])])
        result.append(val)
    except ZeroDivisionError:
        pass
    try:
        val = do_operations_no_paren([s1], [a, s3(s2(b, c), d)])
        result.append(val)
    except ZeroDivisionError:
        pass
    try:
        val = do_operations_no_paren([s1], [a, s2(b, s3(c, d))])
        result.append(val)
    except ZeroDivisionError:
        pass

    return [int(n) for n in result if int(n) == n]

def most_consecutive(dig_cands, sign_cands):
    all_encountered = []
    for perm in all_permutations(dig_cands):
        for sign_set in sign_cands:
            for number in results(sign_set, perm):
                if number > 0 and number not in all_encountered:
                    all_encountered.append(number)
    biggest = 1
    while biggest + 1 in all_encountered:
        biggest = biggest + 1
    return biggest

def main(verbose=False):
    SIGNS = [operator.add, operator.sub, operator.mul, operator.div]
    SIGN_CANDS = []
    for sign1 in SIGNS:
        for sign2 in SIGNS:
            for sign3 in SIGNS:
                SIGN_CANDS.append([sign1, sign2, sign3])
    special_range = [n*1.0 for n in range(1, 10)]
    DIG_CANDS = all_subsets(special_range, 4)

    max_tuple = None
    max_val = 0
    for dig_cand in DIG_CANDS:
        length = most_consecutive(dig_cand, SIGN_CANDS)
        if length > max_val:
            max_val = length
            max_tuple = dig_cand
    return ''.join([str(int(n)) for n in max_tuple])

if __name__ == "__main__":
    print euler_timer(93)(main)(verbose=True)
