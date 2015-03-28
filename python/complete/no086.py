#!/usr/bin/env python

# We have 6 different initial choices
# 3 choices for the face the bug travels on
# and from there 2 choices for which side of
# the face the bug will leave for the last corner
# All 6 permutations of (a, b, c) will make up
# these 6 possibilities, let the bug

# Travel first on the face s_1 x s_2 and then on the
# face s_2 by s_3, and meet the s_2 side a distance
# x from the end furthest from the starting point
# then the squared distance in the first face will be
# d**2 = s_1**2 + (s_2 - x)**2 and along the
# second face will be x**2 + s_3**2

# We have f(x, y) = sqrt(s_1**2 + y**2) + sqrt(s_3**2 + x**2)
# where x + y = s_2. Clearly swapping the roles of
# s_1 and s_3 does nothing so we really only have 3
# possibilites

# Taking derivatives, the minimum occurs at
# x = s_2*s_3/(s_1 + s_3)
# yielding a minimum of sqrt(s_2**2 + (s_1 + s_3)**2)

# Thus the minimum is one of
# a**2 + (b + c)**2 = (a**2 + b**2 + c**2) + 2*b*c
# b**2 + (c + a)**2 = (a**2 + b**2 + c**2) + 2*c*a
# c**2 + (a + b)**2 = (a**2 + b**2 + c**2) + 2*a*b
# If a <= b <= c, a*b <= c*a <= b*c,
# hence the minimum occurs at c**2 + (a + b)**2

# Let SP(M) = #{paths of max size MxMxM with integer shortes path}
# Clearly
# SP(M) = SP(M - 1) + #{paths of size axbxM with integer shortes path | a<=b<=M}

# Initially SP(1) = 0 since the only cube is 1x1x1 and
# the min distance is sqrt(5)

# The difference SP(M) - SP(M - 1) can be computed with the assumption
# that c = M (the largest side) hence we need to find all
# pairs a <= b <= M with (a + b)**2 + M**2 an integer

# clearly 2 <= a + b <= 2*M. Given k = a + b in this range, we have
# k - M <= k - b = a = (a + a)/2 <= (a + b)/2 = k/2

from python.decorators import euler_timer
from python.functions import is_power


def unique_pairs(k, M):
    lower = max(k - M, 1)
    upper = k / 2  # integer division intended
    return upper - lower + 1


def main(verbose=False):
    TARGET = 10 ** 6
    M = 1
    solutions = 0
    while solutions < TARGET:
        M += 1
        # need a + b with (a + b)**2 + M**2
        for inferior_sum in xrange(2, 2 * M + 1):
            if is_power((inferior_sum) ** 2 + M ** 2, 2):
                solutions += unique_pairs(inferior_sum, M)
    return M

if __name__ == '__main__':
    print euler_timer(86)(main)(verbose=True)
