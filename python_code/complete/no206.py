#!/usr/bin/env python

# Find the unique positive integer whose square has the form
# 1_2_3_4_5_6_7_8_9_0,
# where each "_" is a single digit.

# Since n**2 % 10 == 0, we know n = 10**k, hence
# 1_2_3_4_5_6_7_8_9 = k**2
# 10203040506070809 <= k**2 <= 19293949596979899
# 101010101 <= k <= 138902662

from python_code.decorators import euler_timer

def main(verbose=False):
    for n in xrange(101010101, 138902662 + 1):
        if n % 250 in [43, 53, 83, 167, 197, 207]:
            val = n**2
            if str(val)[::2] == '123456789':
                return 10*n

if __name__ == "__main__":
    print euler_timer(206)(main)(verbose=True)
