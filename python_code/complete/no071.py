#!/usr/bin/env python

# neighbors
# a/b < c/d
# need bc - ad = 1

# The converse is also true. If
# bc - ad =  1
# for positive integers a,b,c and d with a < b and c < d then a/b and c/d
# will be neighbours in the Farey sequence of order max(b,d).

# By listing the set of reduced proper fractions for D <= 1,000,000 in
# ascending order of size, find the numerator of the fraction immediately
# to the left of 3/7.

#########################################################
# c = 3, d = 7, 3b - 7a = 1
# 0 + 2a == 1 mod 3, a == 2 mod 3
# a = 3k + 2, b = 7k + 5
# a < b <==> 3k + 2 < 7k + 5, -3 < 4k, -0.75 < k, k >= 0
# a/b < 3/7 <==> 7a < 3b <==> 0 < 3b - 7a <==> ALWAYS
# gcd(a,b) = (3k+2,7k+5) = (3k+2,k+1) = (k,k+1) = 1

# b <= D
# 7k + 5 <= D
# k <= floor((D-5)/7)

from python_code.decorators import euler_timer

def main(verbose=False):
    D = 10**6
    return 3*int((D - 5)/7.0) + 2

if __name__ == '__main__':
    print euler_timer(71)(main)(verbose=True)
