#!/usr/bin/env python

# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
# Not all numbers produce palindromes so quickly. For example,

# 349 + 943 = 1292,
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337

# That is, 349 took three iterations to arrive at a palindrome.

# Although no one has proved it yet, it is thought that some numbers,
# like 196, never produce a palindrome. A number that never forms a
# palindrome through the reverse and add process is called a Lychrel
# number. Due to the theoretical nature of these numbers, and for
# the purpose of this problem, we shall assume that a number is Lychrel
# until proven otherwise. In addition you are given that for every
# number below ten-thousand, it will either (i) become a palindrome
# in less than fifty iterations, or, (ii) no one, with all the computing
# power that exists, has managed so far to map it to a palindrome. In fact,
# 10677 is the first number to be shown to require over fifty iterations
# before producing a palindrome:
# 4668731596684224866951378664 (53 iterations, 28-digits).

# Surprisingly, there are palindromic numbers that are themselves
# Lychrel numbers; the first example is 4994.

# How many Lychrel numbers are there below ten-thousand?

from python.decorators import euler_timer
from python.functions import is_palindrome


def next_lychrel_value(n):
    return n + int(str(n)[::-1])


def update_hash(n, max_iterations, hash_={}):
    """
    Uses the hash values and continually updates
    the sequence until a palindrome is found or until
    the number of iterations exceeds max_iterations
    """
    curr = next_lychrel_value(n)
    to_add = {0: n, 1: curr}
    index = 1
    while not is_palindrome(curr) and index <= max_iterations:
        if curr in hash_:
            covered = hash_[curr].copy()
            for i in range(1, max(covered) + 1):
                to_add[index + i] = covered[i]
            index += max(covered)
        else:
            curr = next_lychrel_value(curr)
            index += 1
            to_add[index] = curr
    hash_[n] = to_add
    return to_add


def main(verbose=False):
    lychrel_sequences = {}
    for i in range(1, 10000):
        update_hash(i, 50, lychrel_sequences)

    # We begin with the inital assumption that every number
    # is a Lychrel number, and reduce the count every time
    # we encounter a number which is not
    count = 9999
    for key, value in lychrel_sequences.items():
        if 50 in value:
            iterations = 50
        else:
            iterations = max(value)

        if is_palindrome(value[iterations]):
            count -= 1

    return count

if __name__ == '__main__':
    print euler_timer(55)(main)(verbose=True)
