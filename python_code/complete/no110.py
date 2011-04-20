from math import floor
from math import log

from python_code.functions import prime_factors
from python_code.functions import sieve

prime_factors_hash = {}

# P^k < 10*7 (10 mil)
thr = [3**exp for exp in range(int(floor(7*log(10)/log(3))) + 1)]
fiv = [5**exp for exp in range(int(floor(7*log(10)/log(5))) + 1)]
sev = [7**exp for exp in range(int(floor(7*log(10)/log(7))) + 1)]
products = []
for f1 in thr:
    for f2 in fiv:
        for f3 in sev:
            products.append(f1*f2*f3)
products = [xx for xx in sorted(products) if xx >= 8*(10**6)][:20]

PRIMES = sieve(100)

max_prod = 10**21
res = []
for product in products:
    factors = prime_factors(product, unique=False, hash_=prime_factors_hash)
    factors = [(factor - 1)/2 for factor in factors][::-1]
    curr_prod = 1
    for i, exp in enumerate(factors):
        curr_prod = curr_prod*(PRIMES[i]**exp)

    if curr_prod < max_prod:
        max_prod = curr_prod
print max_prod
