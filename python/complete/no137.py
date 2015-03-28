#!/usr/bin/env python

# A_F(x) = xF_1 + x^2F_2 + ...
# (x + x^2)A_F(x) = x^2F_1 + x^3F_2 + ... + x^3F_1 + x^4F_2 + ...
# using F_k = F_{k-1} + F_{k-2}, F_1=1, F_2=1
# (x + x^2)A_F(x) = x^2F_1 + x^3F_3 + x^4F_4 + ..
# (x + x^2)A_F(x) = x^2F_1 - xF_1 - x^2F_2 + A_F(x)
# A_F(x) = (-x)/(x^2 + x - 1)

# A_F(x) = n ==> nx^2 + (n+1)x - n = 0
# For x to be rational, we need to discriminant sqrt(b^2 - 4ac)
# to be rational
# D = (n + 1)^2 - 4n(-n) = 5n^2 + 2n + 1 = m^2
# 25n^2 + 10n + 5 = 5m^2
# (5n + 1)^2 + 4 = 5m^2
# 5m^2 - (5n + 1)^2 = 4

# a, b, c, d = 0, 2, 104, 714
# n_prim4 = [0, 2, 104, 714]

from python.conway_topograph import all_values_on_form
from python.conway_topograph import get_recurrence
from python.conway_topograph import start_to_series
from python.decorators import euler_timer
from python.functions import recurrence_next


def golden_nuggets(limit):
    # We seek 5x_k^2 - y_k^2 = 4
    # Where 5n + 1 = y_k
    x_mult, y_mult, relation = get_recurrence([5, -1])
    starting_points = all_values_on_form([5, -1], 4)
    series = [start_to_series(initial, y_mult, 'y')
              for initial in starting_points]
    nuggets = [pair[0] for pair in series
               if pair[0] % 5 == 1 and pair[0] > 1]
    while len(nuggets) < 2 * limit:
        next = [pair[1] for pair in series
                if pair[1] % 5 == 1 and pair[1] > 1]
        nuggets.extend(next)
        series = [recurrence_next(relation, values) for values in series]
    return sorted([(value - 1) / 5 for value in nuggets])[:limit]


def main(verbose=False):
    nuggets = golden_nuggets(15)
    if verbose:
        return '%s.\nAs a check, the 10th golden nugget is calculated ' \
               'to be %s, as stated.' % (nuggets[-1], nuggets[10 - 1])
    else:
        return nuggets[-1]

if __name__ == '__main__':
    print euler_timer(137)(main)(verbose=True)
