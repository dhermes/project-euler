# Forum says 453377 is too big
from python_code.functions import robust_divide
from python_code.functions import sieve

def is_valid(prime):
    if prime in [2, 3, 5]:
        return False
    _, count_2 = robust_divide(prime - 1, 2, include_count=True)
    _, count_5 = robust_divide(prime - 1, 5, include_count=True)
    if prime == (2**count_2)*(5**count_5) + 1:
        return True
    possible_exp = sorted([(2**exp2)*(5**exp5)
                           for exp2 in range(0, count_2 + 1)
                           for exp5 in range(0, count_5 + 1)])
    for exp in possible_exp:
        if (10**exp - 1) % prime == 0:
            return True
    return False

PRIMES = sieve(10**5)
running_sum = 0
for prime in PRIMES:
    if not is_valid(prime):
        running_sum += prime
print running_sum
