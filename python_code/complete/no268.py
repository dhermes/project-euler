#!/usr/bin/env python

# It can be verified that there are 23 positive integers less
# than 1000 that are divisible by at least four distinct primes
# less than 100.

# Find how many positive integers less than 10**16 are divisible
# by at least four distinct primes less than 100.


######################
# 2*3*5*7*11*13*17*19*23*29*31*37*41 = 304250263527210 < 10**16 but
# 304250263527210*43 = 13082761331670030 > 10**16

# Therefore we have at most 13 primes in our products

# Let N_{p_1,...,p_k} = {n | n < L, p_1, ... , p_k all divide n}
# One can easily show N_{p_1,...,p_k} = floor((L - 1)/(p_1*...*p_k))

# By PIE, our desired number is
# sum_{s in S} N_{s}
# where S is the set of all subsets of size 4 of the primes under 100

# Since N_{p1,...,p5} can arise as an intersection of (5 C 4) subsets of
# size 4, we need to subtract off (5 C 4) - 1 = (4 C 3)

# Similarly N_{p1,...,p6} can arise as an intersection of (6 C 4) subsets of
# size 4 of which we've already counted (5 C 4), so we need to add back
# in (6 C 4) - (5 C 4) = (5 C 3), etc.

# In general, we need to add/subtract back (index - 1 C 3)

import operator

from math import log

from python_code.decorators import euler_timer
from python_code.functions import all_subsets
from python_code.functions import choose
from python_code.functions import sieve

def main(verbose=False):
    primes = sieve(100)

    MAX_n = 10**16

    product_factor_pairs = [(1,0)]
    product_hash = {0: [1]}
    for num_factors in range(1, 13 + 1):
        product_hash[num_factors] = []

    # (1,0) becomes
    # (1,0), (p, 1) becomes
    # (1,0), (p, 1), (q,1), (q*p, 2) etc.
    for prime in primes:
        to_add = []
        for product, num_factors in product_factor_pairs:
            if prime*product < MAX_n:
                to_add.append((prime*product, num_factors + 1))
                product_hash[num_factors + 1].append(prime*product)
        product_factor_pairs += to_add

    result = 0
    sign = -1
    for num_factors in range(4, 13 + 1):
        sign = -sign
        PIE_factor = sign*choose(num_factors - 1, 3)
        current_sum = 0
        for product in product_hash[num_factors]:
            current_sum += MAX_n/product # integer division
        result += PIE_factor*current_sum

    return result

if __name__ == "__main__":
    print euler_timer(268)(main)(verbose=True)
