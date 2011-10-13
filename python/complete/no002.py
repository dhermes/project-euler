#!/usr/bin/env python

# Find the sum of all the even-valued terms
# in the sequence which do not exceed four million.

# f_0 = 0, f_1 = 1, f_(n+2) = f_(n+1) + f_n mod 2 generates
# 0, 1, 1, 0, 1, 1, 0, 1, 1, ... mod 2
# The even terms are f_(3k)
# f_(3k+6) = f_(3k+5) + f_(3k+4)
#          = f_(3k+3) + 2*f_(3k+4)
#          = 3*f_(3k+3) + 2*f_(3k+2)
#          = 4*f_(3k+3) + 2*f_(3k+2) - f_(3k+3)
#          = 4*f_(3k+3) + f_(3k)

from python.decorators import euler_timer
from python.functions import recurrence_next

def main(verbose=False):
    a, b = 0, 2
    running_sum = 0
    while b <= 4000000:
        running_sum += b
        a, b = recurrence_next([1,4], [a,b])
    return running_sum

if __name__ == '__main__':
    print euler_timer(2)(main)(verbose=True)


