#!/usr/bin/env python

# no089.txt contains one thousand numbers written in valid,
# but not necessarily minimal, Roman numerals; that is, they
# are arranged in descending units and obey the subtractive
# pair rule (see FAQ for the definitive rules for this problem).

# Find the number of characters saved by writing each of these
# in their minimal form.

# I < V,X
# X < L,C
# C < D,M

from python_code.decorators import euler_timer
from python_code.functions import get_data

VALUES = {'I': 1,
          'V': 5,
          'X': 10,
          'L': 50,
          'C': 100,
          'D': 500,
          'M': 1000}

def pos_neg(val, next):
    if val not in ('I', 'X', 'C') or not next:
        return 1

    if val == 'I' and next in ('V', 'X'):
        return -1
    elif val == 'X' and next in ('L', 'C'):
        return -1
    elif val == 'C' and next in ('D', 'M'):
        return -1
    return 1

def actual(numeral):
    pairs = [(numeral[ind], numeral[ind + 1]) for
             ind in range(len(numeral) - 1)] + \
            [(numeral[-1], None)]
    return sum([VALUES[pair[0]]*pos_neg(*pair) for pair in pairs])

def to_roman(n):
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = ""
    for i in range(len(ints)):
        count = int(n / ints[i])
        result += nums[i] * count
        n -= ints[i] * count
    return result

def main(verbose=False):
    data = [num for num in get_data(89).split("\n") if num]
    original_digits = len("".join([number for number in data]))
    best = [to_roman(actual(numeral)) for numeral in data]
    return original_digits - len("".join([number for number in best]))

if __name__ == '__main__':
    print euler_timer(89)(main)(verbose=True)
