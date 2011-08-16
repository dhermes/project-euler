#!/usr/bin/env python

# Let S_m = (x_1, x_2, ... , x_m) be the m-tuple of positive real
# numbers with x_1 + x_2 + ... + x_m = m for which
# P_m = x_1 * x_2^2 * ... * x_m^m is maximised.

# For example, it can be verified that [P_10] = 4112
# ([] is the integer part function).

# Find SUM[P_m] for 2 <= m <= 15.

######## LAGRANGE ########
# maximize f(x,...) given g(x,....) = c
# set ratio of partials equal to lambda
# Since g = x_1 + ... + x_m
# We need d(P_m)/d(x_i) = i P_m/x_i = lambda
# Hence i/x_i = 1/x_1, x_i = i*x_1
# m = x_1(1 + ... + m) = x_1(m)(m+1)/2
# x_1 = 2/(m + 1)
# P_m = (2/m+1)**(m*(m+1)/2)*(1*2**2*...*m**m)

# P_10 = (2/11)**(55)*(1*4*...*(10**10)) = 4112.0850028536197

import operator

from math import floor

from python_code.decorators import euler_timer

def P(m):
   return reduce(operator.mul,
                 [((2*n)/(1.0*(m + 1)))**n for n in range(1, m + 1)])

def main(verbose=False):
    return int(sum([floor(P(n)) for n in range(2, 16)]))

if __name__ == '__main__':
    print euler_timer(190)(main)(verbose=True)
