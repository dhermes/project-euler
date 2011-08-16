#!/usr/bin/env python

# 1 --> (2,3,4,5,6,7)

# [1] 1
# [2,...,7] 6
# [8,...,19] 12
# [20,...,37] 18
# [38,...,61] 24

# f(k) = 3k^2 - 3k + 1
# f(k) = elements before layer k if k > 0
#Layer 0
#  1 -- (1,1) -- (2,1),(2,2),(2,3),(2,4),(2,5),(2,6)

# Layer 1
#  2 -- (2,1) -- (1,1), (2,2),(2,6), (3,1),(3,2),(3,12) C
#  3 -- (2,2) -- (1,1), (2,1),(2,3), (3,2),(3,3),(3,4) C
#  4 -- (2,3) -- (1,1), (2,2),(2,4), (3,4),(3,5),(3,6) C
#  5 -- (2,4) -- (1,1), (2,3),(2,5), (3,6),(3,7),(3,8) C
#  6 -- (2,5) -- (1,1), (2,4),(2,6), (3,8),(3,9),(3,10) C
#  7 -- (2,6) -- (1,1), (2,5),(2,1), (3,10),(3,11),(3,12) C

# Layer 2
#  8 -- (3,1) -- (2,1),      (3,2),(3,12),(4,1),(4,2),(4,18) C
#  9 -- (3,2) -- (2,1),(2,2),(3,1),(3,3), (4,2),(4,3)
# 10 -- (3,3) -- (2,2),      (3,2),(3,4), (4,3),(4,4),(4,5) C
# 11 -- (3,4) -- (2,2),(2,3),(3,3),(3,5), (4,5),(4,6)
# 12 -- (3,5) -- (2,3),      (3,4),(3,6), (4,6),(4,7),(4,8) C
# 13 -- (3,6) -- (2,3),(2,4)
# 14 -- (3,7) -- (2,4)
# 15 -- (3,8) -- (2,4),(2,5)
# 16 -- (3,9) -- (2,5)
# 17 -- (3,10) -- (2,5),(2,6)
# 18 -- (3,11) -- (2,6)
# 19 -- (3,12) -- (2,6),(2,1)

# 20 -- (4,1) -- (3,)(4,)(5,)
# 21 -- (4,2) --(3,1)(3,2)
# 22 -- (4,3) -- (3,2)(3,3)
# 22 -- (4,4) --

# (n, k) is corner if k % (n - 1) == 1
# A corner is adjacent to 1 block of lower class, 2 of same, and 3 of higher
# the 2 of same will always be (n, k - 1 *wrap*), (n, k + 1 *wrap*)
# (n,1) will always be (n-1,1),(n,0),(n,2),(n+1,0),(n+1,1),(n+1,2)
# Both the n-1 and n+1 grouping will start where the previous one left off

# Only the corners and the final non-corner have a chance at 3 primes
# This is because if we are not either, then they are next to 2 consec. #'s,
# which give a diff. of 1, the other two pairs will give differences that
# differ by one, so at most 1 of each can be prime

##############################
# Case1, k neq 1, corner
##############################
# The corner (n, k) is adjacent to
# (n-1, (k-1)/(n-1)*(n-2) + 1), (n,k-1), (n,k+1)-->don't matter if not end piece
# (n+1, (k-1)/(n-1)*n), (n+1, (k-1)/(n-1)*n + 1), (n+1, (k-1)/(n-1)*n + 2),
# 3*(n - 1)*(n - 2) + 1 + k vs.
# 3*(n - 2)*(n - 3) + 1 + (k - 1)/(n - 1)*(n - 2) + 1,
# 3*(n - 1)*(n - 2) + k,3*(n - 1)*(n - 2) + 2 + k,
# 3*n*(n - 1) + 1 + (k - 1)/(n - 1)*n, 3*n*(n - 1) + 1 + (k - 1)/(n - 1)*n + 1,
# 3*n*(n - 1) + 1 + (k - 1)/(n - 1)*n + 2

# Diffs
# 6*(n - 2) + (k - 1)/(n - 1),
# 1,1,
# 6*(n - 1) + (k - 1)/(n - 1) - 1,
# 6*(n - 1) + (k - 1)/(n - 1),
# 6*(n - 1) + (k - 1)/(n - 1) + 1,
# Only way it can be 3 is if
# c1=6*(n - 2) + (k - 1)/(n - 1),
# c2=6*(n - 1) + (k - 1)/(n - 1) - 1,
# c3=6*(n - 1) + (k - 1)/(n - 1) + 1,
# But if n > 2, c1 prime implies (k-1)/(n-1) == 1,5 mod 6
# implies c2 == 0,4 mod 6, c3 == 0,2 mod 6, so it is never possible
# for n > 2
# For n = 1, 1 works
# For n = 2, of 3,4,5,6,7 none work

##############################
# Case2, k = 1
##############################
# The corner (n, 1) is adjacent to
# (n-1, 1), (n,6*(n-1)), (n,2)--> don't matter if not end piece,
# (n+1, 6*n), (n+1, 1), (n+1, 2),
# 3*(n - 1)*(n - 2) + 2 vs.
# 3*(n - 2)*(n - 3) + 2,
# 3*(n - 1)*(n - 2) + 1 + 6*(n - 1),3*(n - 1)*(n - 2) + 3,
# 3*n*(n - 1) + 1 + 6*n, 3*n*(n - 1) + 2,
# 3*n*(n - 1) + 3

# Diffs
# 6*(n - 2),
# 6*(n - 1) - 1,1
# 6*(2*n - 1) - 1, 6*(n - 1),
# 6*(n - 1) + 1

# c1=6*(n - 1) - 1
# c2=6*(2*n - 1) - 1
# c3=6*(n - 1) + 1

# Start at n = 3 (cases 1 and 2 already done, special cases)

##############################
# Case3
##############################
# The one outlier is the final piece (n, 6*(n - 1))
# When n > 2, this is not 1 mod n - 1, hence not a corner
# This is adjacent to (n,1),(n,6*n-7),(n-1,1),(n-1,6*(n-2)),
# (n+1,6*n),(n+1,6*n-1)

# 3*(n - 1)*(n - 2) + 1 + 6*(n-1) vs.
# 3*(n - 1)*(n - 2) + 1 + 1, 3*(n - 1)*(n - 2) + 6*(n - 1),
# 3*(n - 2)*(n - 3) + 1 + 1, 3*(n - 2)*(n - 3) + 1 + 6*(n-2),
# 3*n*(n - 1) + 1 + 6*n, 3*n*(n - 1) + 6*n

# Diffs
# 6*(n - 1) - 1, 1,
# 6*(2*n - 3) - 1, 6*(n - 1),
# 6*n, 6*n - 1

# c1=6*(n - 1) - 1
# c2=6*(2*n - 3) - 1
# c3=6*n - 1

# Start at n = 3 (cases 1 and 2 already done, special cases)

from python_code.decorators import euler_timer
from python_code.functions import sieve

# 3*(n - 1)*(n - 2) + 2:
# c1=6*(n - 1) - 1 = 6*n - 7
# c2=6*(2*n - 1) - 1=12*n - 7
# c3=6*(n - 1) + 1=6*n - 5

# 3*(n - 1)*(n - 2) + 1 + 6*(n-1):
# c1=6*(n - 1) - 1=6*n - 7
# c2=6*(2*n - 3) - 1=12*n - 19
# c3=6*n - 1=6*n - 1

# in the first two layers only 1 and 2 do as we wish
# from there, first = 8, last = 19 and we can increment
# first by 6*(layer - 1) and last by 6*layer

# The first corner will be FC(layer) = 3*(layer - 1)*(layer - 2) + 2
# it only has PD = 3 if
# (6*layer - 7), (6*layer - 5) and (12*layer - 7) are prime

# The last corner will be
# LC(layer) = 3*(layer - 1)*(layer - 2) + 1 + 6*(layer - 1)
# it only has PD = 3 if
# (6*layer - 7), (6*layer - 1) and (12*layer - 19) are prime

# Instead of carrying out costly multiplications, we can increment
# these by 6 and 12 respectively, similarly
# FC(L + 1) - FC(L) = 6*(L - 1)
# LC(L + 1) - LC(L) = 6*L
# So we can increment these as well

def main(verbose=False):
    TOTAL = 2000
    MAX_n = 10**6
    PRIMES = sieve(MAX_n)
    # Constant, rather than linear lookup
    prime_bools = [False]*(MAX_n + 1)
    for prime in PRIMES:
        prime_bools[prime] = True

    count = 2
    current = 2

    layer = 3
    first_corner = 8 # Value of first corner in layer
    last_corner = 19 # Value of last corner in layer
    six_shared = 11 # prime candidate shared by both corners,
                    # with a difference of 6
    six_first = 13 # prime candidate for first corner, diff 6
    six_last = 17 # prime candidate for last corner, diff 6
    twelve_first = 29 # prime candidate for first corner, diff 12
    twelve_last = 17 # prime candidate for last corner, diff 12
    while count < TOTAL:
        if twelve_first > MAX_n:
            raise Exception("Primes not large enough")
        if prime_bools[six_shared]:
            if prime_bools[six_first] and prime_bools[twelve_first]:
                current = first_corner
                count += 1
            if count < TOTAL:
                if prime_bools[six_last] and prime_bools[twelve_last]:
                    current = last_corner
                    count += 1

        six_shared, six_last = six_last, six_last + 6
        six_first += 6
        twelve_last, twelve_first = twelve_first, twelve_first + 12

        first_corner += 6*(layer - 1)
        last_corner += 6*layer

        layer += 1

    return current

if __name__ == '__main__':
    print euler_timer(128)(main)(verbose=True)
