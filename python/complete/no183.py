#!/usr/bin/env python

# M(N) = max_k (N/k)^k
# This is a discrete function, but its derivative has value
# f(k) = (N/k)^k, ln(f) = k ln(N) - k ln(k)
# f'/f = (ln(f))' = ln(N) - (ln(k) + k(1/k)) = ln(N/k) - 1
# f' > 0 iff ln(N/k) > 1 iff N/e > k
# So f increases towards N/e and similar decreases away from N/e
# Hence the max occurs either at the ceiling or floor of N/e

# Let k_star(N) be the function such that
# M(N) = P_max = f(k_star(N))

# Since the numerator of P_max is k_star**k_star, M(N) is only
# terminating if k_star is completely composed of 2's and 5's
# With this in mind, we defind k_reduced(N) to be the quotient
# that remains after all 2's and 5's are divided from k_star(N)
# Finally, D(N) = -N iff M(N) is terminating iff k_reduced(N) = 1

from fractions import gcd
from math import ceil
from math import e as EULER_e
from math import floor

from python.decorators import euler_timer
from python.functions import robust_divide

def k_star(N):
    k_1 = int(floor(N/EULER_e))
    k_2 = int(ceil(N/EULER_e))
    if k_1 == k_2:
        return k_1
    elif k_2 - k_1 != 1:
        raise ValueError("Bad info with %s" % N)
    return k_1 if (k_1 + 1)**(k_1 + 1) > N*(k_1**k_1) else k_2

def k_reduced(N):
    k_st = k_star(N)
    k_induced = robust_divide(robust_divide(k_st, 5), 2)
    shared_factors = gcd(k_induced, N)
    return k_induced/shared_factors

def D(N):
    sign = 1 if k_reduced(N) > 1 else -1
    return sign*N

def main(verbose=False):
    MAX_N = 10**4
    return sum(D(N) for N in range(5, MAX_N + 1))

if __name__ == '__main__':
    print euler_timer(183)(main)(verbose=True)
