#!/usr/bin/env python

# Consider isosceles (b, L, L) with height h to b
# b = 16, L = 17 gives h = 15
# b = 272, L = 305 gives h = 273

# Find SUM(L) for the twelve smallest isosceles triangles for which
# h = b +/- 1 and b, L are positive integers.

#############################
# This is a question of quadratic forms
# L**2 = h**2 + (b/2)**2
# If b is odd, then we get a pythagorean triple
# (2L, 2h, b) which reduces to primitive (X, Y, b')
# Since it can only reduce by factors of b, we know
# 1) b' is odd and
# 2) no even factors were removed from 2L or 2h,
#    forcing X and Y to be even
# This is a contradiction since no primitive pythagorean
# triple has odd hypotenuse (can check)

# So set
# b = 2*B, h = 2*B + sign = 2*B + s
# B**2 + (2*B + s)**2 = L**2
# B**2 + (4*B**2 + 4*B*s + 1) = L**2
# 25*B**2 + s*20*B + 4 + 1 = 5*L**2
# 5*(L**2) - (5*B + 2*s)**2 = 1

from python.conway_topograph import all_values_on_form
from python.conway_topograph import get_recurrence
from python.conway_topograph import start_to_series
from python.decorators import euler_timer
from python.functions import recurrence_next


def solutions(limit):
    # We seek 5x_k^2 - y_k^2 = 1
    # Where L = x_k
    x_mult, y_mult, relation = get_recurrence([5, -1])
    starting_points = all_values_on_form([5, -1], 1)
    series = [start_to_series(initial, x_mult, 'x')
              for initial in starting_points]
    result = [pair[0] for pair in series if pair[0] > 1]
    while len(result) < 2 * limit:
        next = [pair[1] for pair in series if pair[1] > 1]
        result.extend(next)
        series = [recurrence_next(relation, values) for values in series]
    return sorted(result)[:limit]


def main(verbose=False):
    # smallest 12 solutions returned in solutions(12)
    return sum(solutions(12))

if __name__ == '__main__':
    print euler_timer(138)(main)(verbose=True)
