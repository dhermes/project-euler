#!/usr/bin/env python

# It is possible to show that the square root of two can be expressed as
# an infinite continued fraction.

# sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ...))) = 1.414213...

# By expanding this for the first four iterations, we get:
# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

# The next three expansions are 99/70, 239/169, and 577/408, but the eighth
# expansion, 1393/985, is the first example where the number of digits in
# the numerator exceeds the number of digits in the denominator.

# In the first one-thousand expansions, how many fractions contain a numerator
# with more digits than denominator?

from python_code.decorators import euler_timer
from python_code.functions import recurrence_next

# We can write the rth expansion as h_r/k_r where both h and k satisfy
# f(n+2) = 2f(n+1) + f(n)
# and h_0 = 1, h_1 = 3, k_0 = 1, k_1 = 2
def main(verbose=False):
    relation = [1, 2]

    h_values = [1, 3]
    k_values = [1, 2]

    count = 0
    for i in range(2, 1000 + 1):
        h_values = recurrence_next(relation, h_values)
        k_values = recurrence_next(relation, k_values)
        if len(str(h_values[1])) > len(str(k_values[1])):
            count += 1

    return count

if __name__ == "__main__":
    print euler_timer(57)(main)(verbose=True)
