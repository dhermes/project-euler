#!/usr/bin/env python

# Starting with 1 and spiralling anticlockwise in the following way, a square
# spiral with side length 7 is formed.
#
# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49
#
# It is interesting to note that the odd squares lie along the bottom right
# diagonal, but what is more interesting is that 8 out of the 13 numbers lying
# along both diagonals are prime; that is, a ratio of 8/13 or approx. 62%.

# If one complete new layer is wrapped around the spiral above, a square
# spiral with side length 9 will be formed. If this process is continued, what
# is the side length of the square spiral for which the ratio of primes along
# both diagonals first falls below 10%?

# ALGORITHM:
# The corners are as follows:
# 1-(3-5-7-9)-(13-17-21-25)-(31-37-43-49)-...
# Each set of four corners has an associated side
# length and each new layer needs to be taken into
# consideration

# We can represent each layer as such:
# (index, last, primes)
# For example the first "layer" is just the number 1
# index = 1 for first layer
# last = 1 for the last corner in the layer
# primes = 0 since we have encountered no primes on the "corners"

# To get from the last in a layer to the first corner in the next layer
# one needs to go right one square and then go the entire length of
# the side, less one, since coming from the inside layer. Hence, the first
# corner is the same distance from the last in the previous layer as the
# other three corners are than their previous counterparts.
# It takes 0 steps to walk along a side in Layer 1 (the single 1) .
# As we add a layer, we add both top and bottom, both left and right, hence
# this walk increases by 2. In general, layer (i+1) will take 2*i steps
# With that in mind, (index, last) gives rise to the next four corners
# C1 = last + #steps = last + 2*index (since in layer index + 1)
# C2 = C1 + #steps, etc. gives
# [last + 2*index*i for i in range(1,5)]

# Since layer 1 is (1, 1, 0)
# From here, the next layer is [1 + 2*1*i for i in range(1,5)] = [3, 5, 7, 9]
# We can represent this layer similarly as (2, 9, 3) since the last corner
# is 9 and 3,5 and 7 are all prime
# The next layer is [9 + 2*2*i] = [13,17,21,25] which yields (3, 25, 5)

# Since the side length includes both corners, we know the side length
# to be 2*(index - 1) + 1 (THIS IS USED TO COMPUTE THE ANSWER)
# Also, since we add 4 corners at each step and start with 1, we have
# 4*index - 3 total corners at a given step
# Also notice that last[index] = (2*index - 1)**2, hence can
# never be prime (can prove easily by induction)

from math import sqrt

from python.decorators import euler_timer
from python.functions import is_prime
from python.functions import sieve


def main(verbose=False):
    # layer/primes
    #     2/3
    #  1581/835
    #  3536/1677
    #  5000/2249
    # 13121/5248, winning layer

    # ratio >= .1 iff 10*(primes/total) >= 1 iff 10*primes >= total
    # iff 10*primes >= 4*index - 3
    FAILURE_POINT = 10 ** 9
    PRIMES = sieve(int(sqrt(FAILURE_POINT)) + 1)

    layer = 2
    num_primes = 3
    while 10 * num_primes >= 4 * layer - 3:
        layer += 1
        candidates = [(2 * layer - 1) ** 2 - 2 * (layer - 1) * i
                      for i in range(1, 4)]
        if candidates[-1] >= FAILURE_POINT:
            raise ValueError("Sieve was not big enough, restart function")
        for candidate in candidates:
            if is_prime(candidate, primes=PRIMES, failure_point=FAILURE_POINT):
                num_primes += 1
    side_length = 2 * layer - 1  # 2*(layer - 1) + 1
    return side_length

if __name__ == '__main__':
    print euler_timer(58)(main)(verbose=True)
