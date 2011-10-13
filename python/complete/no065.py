#!/usr/bin/env python

# The square root of 2 can be written as an infinite continued fraction.
# sqrt(2) = [1;(2)]

# It turns out that the sequence of partial values of continued fractions
# for square roots provide the best rational approximations. Let us
# consider the convergents for sqrt(2).

# 1 + 1/2 = 3/2
# 1 + 1/(2 + 1/2) = 7/5
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29

# What is most surprising is that the important mathematical constant,
# e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

# The first ten terms in the sequence of convergents for e are:

# 2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

# The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

# Find the sum of digits in the numerator of the 100th convergent of the
# continued fraction for e.

# We can show (but won't) that the sequence of convergents
# h_0/k_0, h_1/k_1, h_2/k_2, h_3/k_3, h_4/k_4, ...
# satisfies h_n = a_n h_(n-1) + h_(n-2) (and similar for k) with
# h_(-1) = 1, h_(-2) = 0, k_(-1) = 0, k_(-2) = 1

import operator

from fractions import gcd

from python.decorators import euler_timer
from python.functions import recurrence_next

def main(verbose=False):
    # we have h_(-1) = 1, k_(-1) = 0
    # h_0/k_0 = 2
    h_values = [1, 2]
    k_values = [0, 1]

    # The problem wants the 100th convergent which will
    # be h_99/k_99. To get to this, we need the first 99
    # values of a
    a = reduce(operator.add, [[1,2*k,1] for k in range(1, 33 + 1)])
    for a_i in a:
        relation = [1, a_i]
        h_values = recurrence_next(relation, h_values)
        k_values = recurrence_next(relation, k_values)

    h_99 = h_values[1]
    k_99 = k_values[1]
    reduced = h_99/(gcd(h_99, k_99))
    return sum([int(dig) for dig in str(reduced)])

if __name__ == '__main__':
    print euler_timer(65)(main)(verbose=True)
