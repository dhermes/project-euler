#!/usr/bin/env python

# Beginning with the trivial [[0,1]], we can
# loop through all primes and elect to add
# a new prime or not, branching the recursion
# at each step and updating the final sum

# Example:
# sum = 0

# Branch 1 (pairs=[[0,1]], primes = [5,13]):
# 5 out
# pairs = [[0,1]], primes = [13] --> 2a
# don't contribute to sum
# or
# 5 in
# pairs = [[1,2]], primes = [13] --> 2b
# add sum([1]) to sum, sum = 1

# Branch 2a (pairs=[[0,1]], primes = [13]):
# 13 out
# pairs = [[0,1]], primes = [] --> No branch
# don't contribute to sum
# or
# 13 in
# pairs = [[2,3]], primes = [] --> No branch
# add sum([2]) to sum, sum = 3

# Branch 2b (pairs=[[1,2]], primes = [13]):
# 13 out
# pairs = [[1,2]], primes = [] --> No branch
# don't contribute to sum
# or
# 13 in
# pairs = [[1,8], [4,7]], primes = [] --> No branch
# add sum([1,4]) to sum, sum = 8

# No branches remaining, so final value is 8.

# As a check, we have 5, 13, and 65 which can be decomposed
# as 5 = 1**2 + 2**2, 13 = 2**2 + 3**2, and
# 65 = 1**2 + 8**2 = 4**2 + 7**2, hence 1 + 2 + 1 + 4 = 8 is correct

from math import sqrt

from python.decorators import euler_timer
from python.functions import sieve

def find_raw_solution(prime):
    max_n = int(sqrt(prime))
    for x in range(1, max_n + 1):
        y = int(sqrt(prime - x**2))
        if x**2 + y**2 == prime:
            return [x, y]
    return None

# Using
# (a**2 + b**2)*(c**2 + d**2) = (a*c - b*d)**2 + (a*d + b*c)**2
#                             = (a*c + b*d)**2 + (a*d - b*c)**2
# Clearly, combining two nontrivial (sorted) pairs gives rise to
# two more sorted pairs
def multiply_pair(pair1, pair2):
    a, b = pair1
    c, d = pair2

    first_pair = sorted([abs(a*c - b*d), a*d + b*c])
    second_pair = sorted([a*c + b*d, abs(a*d - b*c)])
    if first_pair == second_pair:
        return [first_pair]
    else:
        return [first_pair, second_pair]

def squarefree_sum(pairs, primes):
    result = 0
    # Here is the branch point, add the next prime or don't
    # If we don't, there is no need to sum the values
    if primes == []:
        return result


    next_pairs = []
    prime_pair = find_raw_solution(primes[0])
    remaining_primes = primes[1:]
    for pair in pairs:
        new_pairs = multiply_pair(pair, prime_pair)
        result += sum([new_pair[0] for new_pair in new_pairs])
        next_pairs.extend(new_pairs)
    # next_pairs has the prime added
    result += squarefree_sum(next_pairs, remaining_primes)
    # Don't add the prime
    result += squarefree_sum(pairs, remaining_primes)
    return result

def main(verbose=False):
    primes = [prime for prime in sieve(150)
              if prime % 4 == 1]
    initial = [[0, 1]]
    return squarefree_sum(initial, primes)

if __name__ == '__main__':
    print euler_timer(273)(main)(verbose=True)
