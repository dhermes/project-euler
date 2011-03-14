# Define a juncture J to be the four cells straddling a river
# We write J = (B, P, N, F) where B is the cell back,
# P/N are the positive/negative cells
# and F is the forward cell along the river

# A cell has ( (x, y), val ) where (x,y) is the point on the
# lattice and val is the value it takes on the quadratic form

# While traversing the river, if the value of F is positive,
# we turn right, if it is negative we turn left
# To turn left is: (B, P, N, F) -> (N, P, F, P + F)
# To turn right is: (B, P, N, F) -> (P, F, N, N + F)
# It can be thought of like this: the forward value must lie on
# the river (if a river exists), hence it must become the next
# positive cell in the juncture or the next negative cell

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
