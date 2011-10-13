#!/usr/bin/env python

# Find the sum of all the numbers that can be written
# as the sum of fifth powers of their digits.

# n =  d-digits, sum(n) <= d*9^5 = 59049d, n >= 10^(d-1),
# so sum(n) = n implies 10*(9**5 d) >= 10**d,
# ln(10 * 9**5) + ln(d) >= d ln(10), so d <= 6

from python.decorators import euler_timer

def sum_of_digits_powers(n, power):
    return sum([int(dig)**power for dig in str(n)])

def main(verbose=False):
    valid = []
    for i in xrange(2,999999 + 1):
        if sum_of_digits_powers(i, 5) == i:
            valid.append(i)

    if verbose:
        return '%s.\nThe numbers satisfying this property are: %s.' % (
            sum(valid), ', '.join([str(num) for num in valid]))
    else:
        return sum(valid)

if __name__ == '__main__':
    print euler_timer(30)(main)(verbose=True)
