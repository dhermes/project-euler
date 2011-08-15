#!/usr/bin/env python

# It is well known that if the square root of a natural number is not an
# integer, then it is irrational. The decimal expansion of such square
# roots is infinite without any repeating pattern at all.

# The square root of two is 1.41421356237309504880..., and the digital
# sum of the first one hundred decimal digits is 475.

# For the first one hundred natural numbers, find the total of the digital sums
# of the first one hundred decimal digits for all the irrational square roots.

###########################
# To deal with precision, we use no064 and no065 to help out.
# The expanded_digits function will expanded n/d to d digits no matter
# the precision simply by multiplying by 10

# We use the cycle (algorithm calculated in 64) to find the values of a_i
# in the continued fraction expansion and we use the recurrence on
# the numerator and denominator in the fractional estimate as in
# 65. Once these estimates agree to 100 digits, we stop

from python_code.decorators import euler_timer
from python_code.functions import continued_fraction_cycle
from python_code.functions import is_power
from python_code.functions import recurrence_next

def expanded_digits(numerator, denominator, digits):
    # use integer division on num and denom to get a quotient
    quotient_digits = [int(dig) for dig in str(numerator/denominator)]
    remainder = numerator % denominator
    if len(quotient_digits) >= digits:
        return quotient_digits[:digits]
    return quotient_digits + expanded_digits(10*remainder,
                                             denominator,
                                             digits - len(quotient_digits))

def stable_expansion(digits, n):
    values = continued_fraction_cycle(n)
    h_values = [1, values[0]] # a_0
    k_values = [0, 1]

    cycle_length = len(values) - 1 # we only cycle over a_1,...,a_{k-1}
    last = expanded_digits(h_values[1], k_values[1], digits)
    index = 1
    relation = [1, values[index]]
    h_values = recurrence_next(relation, h_values)
    k_values = recurrence_next(relation, k_values)
    current = expanded_digits(h_values[1], k_values[1], digits)
    while current != last:
        index += 1
        last = current

        relative_index = ((index - 1) % cycle_length) + 1
        # we want residues 1,..,k-1 instead of the traditional 0,...,k-2
        relation = [1, values[relative_index]]
        h_values = recurrence_next(relation, h_values)
        k_values = recurrence_next(relation, k_values)
        current = expanded_digits(h_values[1], k_values[1], digits)
    return current

def main(verbose=False):
    non_squares = [num for num in range(1, 100 + 1)
                   if not is_power(num, 2)]
    running_sum = 0
    for n in non_squares:
        running_sum += sum(stable_expansion(100, n))
    return running_sum

if __name__ == "__main__":
    print euler_timer(80)(main)(verbose=True)
