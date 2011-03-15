# Define a juncture J to be the four cells straddling a river
# We write J = (B, P, N, F) where B is the cell back,
# P is the cell "above" the middle and "N" the cell below
# (we often think of them as the positive/negative cells since
# the serve that purpose along the river)
# and F is the forward cell

# A cell has ( (x, y), val ) where (x,y) is the point on the
# lattice and val is the value it takes on the quadratic form

# RIVER:
# While traversing a river, if the value of F is positive,
# we turn right, if it is negative we turn left
# To turn left is: (B, P, N, F) -> (N, P, F, P + F)
# To turn right is: (B, P, N, F) -> (P, F, N, N + F)
# It can be thought of like this: the forward value must lie on
# the river (if a river exists and we are already on it), hence
# it must become the next positive cell in the juncture or the
# next negative cell

# POSITIVE ROOT:
# Define a positive root to be a point on the river where two
# positive valued cells meet, from which going forward all
# values must increase (since on the river, the value behing
# the two positives must be negative)

import operator
from math import sqrt

from python_code.functions import factors
from python_code.functions import is_power

def plus(cell1, cell2, back_val):
    """
    Moves forward between two cells. Requires a third cell, though
    truly only requires the value of that the form takes at
    the cell.
    """
    (x1, y1), val1 = cell1
    (x2, y2), val2 = cell2
    # back_val, val1 + val2, val form an arithmetic progression
    val = 2*(val1 + val2) - back_val
    x = x1 + x2
    y = y1 + y2
    return ( (x, y), val)

def next_juncture_on_river(juncture):
    """
    Moves along the river to the next juncture

    Turns "left" if the forward value if negative
    and "right" if it is positive
    """
    B, P, N, F = juncture
    forward_val = F[1]
    if forward_val < 0:
        # turn left
        NEXT = plus(P, F, N[1])
        return (N, P, F, NEXT)
    elif forward_val > 0:
        # turn right
        NEXT = plus(N, F, P[1])
        return (P, F, N, NEXT)
    else:
        raise Exception("No infinite river here, found a lake.")

def juncture_isom(juncture1, juncture2):
    """Takes a juncture and checks if the cell values are all equal"""
    B1, P1, N1, F1 = juncture1
    B2, P2, N2, F2 = juncture2
    return ((B1[1] == B2[1]) and (P1[1] == P2[1]) and
            (N1[1] == N2[1]) and (F1[1] == F2[1]))

def seek_up_to_val(juncture, max_value):
    """
    Returns all cells sprouting forth from a positive root
    up to a cell value of max_value

    Takes advantage of fact that all values must increase away
    from the river (on positive side)
    """
    B, P, N, F = juncture
    if F[1] > max_value:
        return []
    result = [F]

    turn_left = plus(P, F, N[1])
    J_left = (N, F, P, turn_left)
    result.extend(seek_up_to_val(J_left, max_value))

    turn_right = plus(N, F, P[1])
    J_right = (P, F, N, turn_right)
    result.extend(seek_up_to_val(J_right, max_value))
    return result

def all_positive_roots(form):
    """
    Takes a quadratic form and gives all the
    "positive roots" along the river

    Form is the coefficients on x and y
    e.g. if [a,b] = form, f(x,y) = ax**2 + by**2
    """
    a, b = form
    B = ((1, -1), a + b)
    P = ((1, 0), a)
    N = ((0, 1), b)
    F = ((1, 1), a + b)
    J_init = (B, P, N, F)

    new_positives = []
    J_curr = next_juncture_on_river(J_init)
    # traverse the river until back to the beginning
    while not juncture_isom(J_init, J_curr):
        # we add a new positive if the forward
        # value is positive
        if J_curr[-1][1] > 0:
            new_positives.append(J_curr)
        J_curr = next_juncture_on_river(J_curr)

    # For each (B, P, N, F) in new_positives, we want to
    # transform to a root for positive values, which will
    # be (N, P, F, new_cell)
    result = []
    for new_positive in new_positives:
        B, P, N, F = new_positive
        new_cell = plus(P, F, N[1])
        result.append((N, P, F, new_cell))
    return result

def all_values_on_form(form, value):
    """
    Returns all lattice points (not necessarily coprime)
    that produce the desired value on the form

    Given the recurrence for the form, these values
    can serve to determine *all* solutions for
    the given value due to the repeating nature
    of the infinite river
    """
    factor_list = factors(value)
    valid_factors = [factor for factor in factor_list
                     if is_power(value/factor, 2)]

    roots = all_positive_roots(form)
    found = set()
    for root in roots:
        candidates = seek_up_to_val(root, value)
        to_add = [candidate for candidate in candidates
                  if candidate[1] in valid_factors] + \
                 [candidate for candidate in root
                  if candidate[1] in valid_factors]
        found.update(to_add)
    found = list(found)

    # We may get some duplicates from since when we include
    # values from the river, we don't check that they come from
    # a different iteration of the river
    x_mult, y_mult, _ = get_recurrence(form)
    checked = found[:]
    for candidate in found:
        coords, val = candidate
        next_x = sum([operator.mul(*pair) for pair in zip(coords, x_mult)])
        next_y = sum([operator.mul(*pair) for pair in zip(coords, y_mult)])
        if ((next_x, next_y), val) in found:
            checked.remove(((next_x, next_y), val))

    # Finally we must scale up factors to account for
    # the reduction by a square multiple
    result = []
    for cell in checked:
        (x, y), val = cell
        if val < value:
            ratio = int(sqrt(value/val))
            x *= ratio
            y *= ratio
        result.append((x,y))

    return result

def get_recurrence(form):
    """
    Input: quadratic form [a,b]

    Output: (y_mult, y_mult, relation) where y_mult is the coefficients
    of x and y (respectively) that lead to the recurrence on the
    lattice to the next x value (from a previous (x,y) tuple),
    y_mult is the analogue for the y value and relation is
    the recurrence relation on each coordinate (degree 2 recurrence)
    """
    a, b = form
    B = ((1, -1), a + b)
    P = ((1, 0), a)
    N = ((0, 1), b)
    F = ((1, 1), a + b)
    J_init = (B, P, N, F)
    J_curr = next_juncture_on_river(J_init)
    # traverse the river until back to the beginning
    while not juncture_isom(J_init, J_curr):
        J_curr = next_juncture_on_river(J_curr)

    # Here (1,0) --> P = (a,b)
    # and (0,1) --> N = (c,d)
    # (x,y)-->x(a,b)+y(c,d)
    # x-->ax+cy
    # y-->bx+dy
    # x_{n+2}-ax_{n+1} - d(x_{n+1}-ax_n)
    # = cy_{n+1} - d(cy_n) = c(bx_n)
    # x_{n+2} = (cb - ad)x_n + (a+d)x_{n+1}
    # Similarly for y (can check if you want)
    a, b = J_curr[1][0]
    c, d = J_curr[2][0]
    return ((a, c), (b, d), (c*b - a*d, a + d))

def start_to_series(initial, multiplier, series='x'):
    """
    Input: initial is an initial lattice point; multiplier
    is either x_mult (or y_mult) which will transform a point
    to the next x (or y) value on the river; series is
    either x or y to determine which point is used

    Output: the first two values in the series which will determine
    all x (or y values) given the recurrence for the form
    """
    next = sum([operator.mul(*pair) for pair in zip(initial, multiplier)])
    if series == 'x':
        return [initial[0], next]
    elif series == 'y':
        return [initial[1], next]
    else:
        raise ValueError("Unrecoginized series type %s" % series)
