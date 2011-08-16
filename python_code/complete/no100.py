#!/usr/bin/env python

# If a box contains twenty-one coloured discs, composed of fifteen blue
# discs and six red discs, and two discs were taken at random, it can be
# seen that the probability of taking two blue discs,
# P(BB) = (15/21)(14/20) = 1/2.

# The next such arrangement, for which there is exactly 50% chance of taking
# two blue discs at random, is a box containing eighty-five blue discs and
# thirty-five red discs.

# By finding the first arrangement to contain over 10**12 = 1,000,000,000,000
# discs in total, determine the number of blue discs that the box
# would contain.

# (b(b-1))/(T(T-1)) = (1/2) <==> 2(4b**2 - 4b) = 4T**2 - 4T
# <==> 2(2*b - 1)**2 - (2*T - 1)**2 = 1
# One can verify 2*x**2 - y**2 = 1 implies that x and y must be odd
# so all solutions of this are desired by us

from math import sqrt

from python_code.conway_topograph import all_values_on_form
from python_code.conway_topograph import get_recurrence
from python_code.conway_topograph import start_to_series
from python_code.decorators import euler_timer
from python_code.functions import recurrence_next

def main(verbose=False):
    # y = 2T - 1, T > 10**12 implies the following:
    LOWER_LIMIT = 2*(10**12) - 1

    # We seek 2x^2 - y^2 = 1
    x_mult, y_mult, relation = get_recurrence([2, -1])
    starting_points = all_values_on_form([2, -1], 1)
    series = [start_to_series(initial, y_mult, 'y')
              for initial in starting_points]
    result = [pair[0] for pair in series]
    while max(result) <= LOWER_LIMIT:
        result.extend([pair[1] for pair in series])
        series = [recurrence_next(relation, values) for values in series]

    min_y = min([y for y in result if y > LOWER_LIMIT])
    min_x = sqrt((1 + y**2)/2)
    return int((min_x + 1)/2)

if __name__ == '__main__':
    print euler_timer(100)(main)(verbose=True)
