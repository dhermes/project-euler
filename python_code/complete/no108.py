from math import floor
from math import log

from python_code.functions import prime_factors
from python_code.functions import sieve

prime_factors_hash = {}
n = 4
solutions = 3
while solutions < 2000:
    n += 1
    factors = prime_factors(n, unique=False, hash_=prime_factors_hash)
    solutions = 1
    curr_prime = factors[0]
    count = 1
    for prime in factors[1:]:
        if prime == curr_prime:
            count += 1
        else:
            solutions = solutions*(2*count + 1)
            curr_prime = prime
            count = 1
    solutions = solutions*(2*count + 1)
    print n, solutions

print n
