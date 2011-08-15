#!/usr/bin/env python

# A bag contains one red disc and one blue disc. In a game of chance a player
# takes a disc at random and its colour is noted. After each turn the disc is
# returned to the bag, an extra red disc is added, and another disc is
# taken at random.

# The player... wins if they have taken more blue discs than red discs a
# the end of the game.

################################################################################
# P_n = prob(disc n is blue) = 1/(n + 1)

# For n discs, let C_1-C_2-...-C_n be the colors drawn, let i_1,...,i_k be the
# indices j such that disk i_j was drawn red. The probability of this event
# is (i_1 * ... * i_k)/factorial(n + 1)

# We can enumeratively define n_{j,k} to be the aggregate numerator
# of all possible draws with j blues drawn out of k draws
#
# The initial conditions are n_{0,1} = 1, n_{1,1} = 1
# The recurrence is defined by the fact that the n_{j + 1,k + 1} is
# can only have the (k + 1)'st element be blue or red, hence
# n_{j + 1,k + 1} = numer(blue)*n_{j,k} + numer(red)*n_{j + 1,k}
#                 = n_{j,k} + (k + 1)*n_{j + 1,k}
# except for the cases j = k, where n_{j,k} = numer(all blue) = 1
# except for the cases j = 0, where n_{0,k} = k!

from math import factorial

from python_code.decorators import euler_timer

def iterative_numerator(n):
    numerators = {}
    for k in range(1,n + 1):
        for j in range(k + 1):
            if j == 0:
                numerators[(j,k)] = factorial(k)
            elif j == k:
                numerators[(j,k)] = 1
            else:
                numerators[(j,k)] = numerators[(j - 1,k - 1)] + \
                                    k*numerators[(j,k - 1)]
    min_blue = (n/2) + 1
    count = 0
    for blue in range(min_blue, n + 1):
        count += numerators[(blue, n)]
    return count

def max_payout(n):
    # Integer division precludes floor operation
    return factorial(n + 1)/iterative_numerator(n)

def main(verbose=False):
    return max_payout(15)

if __name__ == "__main__":
    print euler_timer(121)(main)(verbose=True)
