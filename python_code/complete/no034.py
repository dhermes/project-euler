#!/usr/bin/env python

# Find the sum of all numbers which are equal to the sum
# of the factorial of their digits.

# We know if n has d digits, then sum(n) <= d*9! = 362880d and n >= 10*(d-1)
# hence sum(n) = n implies 3628800d >= 10^d. We must have d <= 7.

from math import factorial

from python_code.decorators import euler_timer
from python_code.functions import ascending

def main(verbose=False):
    result = []
    # We have at most 7 digits, so we consider all ascending
    # lists of digits with a digit sum between 1 and 63.
    # Since ascending requires the first element of the digit lists
    # is *equal to* the minimum, we allow an 8th digit which is
    # simply a padded zero
    for digit_sum in range(1, 63 + 1):
        for choice in ascending(8, digit_sum, 0, 9):
            choice = choice[1:]
            non_zero = [digit for digit in choice if digit != 0]
            factorial_sum = sum([factorial(digit) for digit in non_zero])
            possible_zeros = 7 - len(non_zero)

            # Can fill out the number with zeros (up to 7 digits)
            for zeros_add in range(possible_zeros + 1):
                factorial_digits = [int(digit) for digit in str(factorial_sum)]
                if sorted(factorial_digits) == sorted(non_zero + [0]*zeros_add):
                    result.append(factorial_sum)

                factorial_sum += 1 # Add factorial(0)

    result = [val for val in result if val not in [1, 2]]

    if verbose:
        return "%s.\nThe full list of numbers is as follows: %s." % (
            sum(result), ", ".join([str(number) for number in result]))
    else:
        return sum(result)

if __name__ == '__main__':
    print euler_timer(34)(main)(verbose=True)
