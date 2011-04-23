from python_code.functions import sieve
from python_code.functions import inverse_mod_n

PRIMES = sieve(10**7)
running_sum = 0
for prime in PRIMES:
    if prime not in [2, 5]:
        running_sum += inverse_mod_n(10, prime)
print running_sum
