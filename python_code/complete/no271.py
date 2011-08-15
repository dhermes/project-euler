#!/usr/bin/env python

# P = f_1*...*f_k, where (f_i, f_j) = 1 if i != j
# This forces (f_i, P/f_i) = 1, hence there
# exist s, r that satisfy:
# s (P/f_i) + r f_i = 1
# Set e_i = s (P/f_i)
# Then e_i + 0 == 1 mod f_i
# and by definition e_i = s*(P/f_i) = s*0 mod f_j for all j != i

# For any x**3 == 1 mod n, we know (x, n) = 1 since x has finite
# order mod n. Thus by CRT, x = (x_1 mod f_1, ..., x_k mod f_k)
# for the coprime factors f_1*...*f_k = n. Given units as
# above, the sum X = e_1*x_1 + ... + e_k*x_k, necessarily has
# X mod f_i = 0*x_1 + ... + 1*x_i + ... + 0*x_k = x_i, hence X = x.

# Thus we need to find all cube roots in the factors dividing our n,
# all of which happen to be prime. We can then combine all possiblities
# to reconstruct X and then sum the X values

from itertools import product as i_product

from python_code.decorators import euler_timer
from python_code.functions import extended_euclid
from python_code.functions import prime_factors

def find_cube_roots(prime):
    # Won't check, but assumes prime is prime
    # in a prime field x^3 == 1 implies x == 1 or x^2 + x + 1 == 0
    # since a domain, the latter is satisfied if
    # (2x + 1)**2 == -3 mod prime (so we handle 2 and 3 differently)
    if prime in [2, 3]:
        return [1]

    # The inverse of 2 is (prime + 1)/2
    # If L(q,p) is the legendre symbol, for p != 2 or 3 we know
    # L(-3, p) = L(-1, p)*L(3, p) = (-1)**(floor((p+1)/6)+(p-1)/2)
    if (-1)**((prime + 1)/6 + (prime - 1)/2) == -1:
        return [1]

    for i in xrange(1, prime):
        if (i**2 + 3) % prime == 0:
            break
    # So we know i and prime - i are the square roots of 3
    return sorted([1,
                   ((prime + 1)*(i - 1)/2) % prime,
                   ((prime + 1)*(prime - i - 1))/2 % prime])

def main(verbose=False):
    product = 13082761331670030
    factors = prime_factors(product)

    candidate_lists = []
    for factor in factors:
        candidate_lists.append([(factor, root)
                                for root in find_cube_roots(factor)])

    result = list(i_product(*candidate_lists))

    coprime_units = {}
    for factor in factors:
        _, multiplier = extended_euclid(factor, product/factor)
        coprime_units[factor] = multiplier*(product/factor)

    vals = []
    for pairing in result:
        count = 0
        for prime, residue in pairing:
            count += residue*coprime_units[prime]
        count = count % product
        vals.append(count)

    return sum(vals) - 1 # 1 is in there as (1,1,...,1)

if __name__ == "__main__":
    print euler_timer(271)(main)(verbose=True)
