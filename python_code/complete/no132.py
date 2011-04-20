# Forum says 453377 is too big
from python_code.functions import robust_divide
from python_code.functions import sieve

def is_valid(prime):
    _, count_2 = robust_divide(prime - 1, 2, include_count=True)
    count_2 = min(9, count_2)
    _, count_5 = robust_divide(prime - 1, 5, include_count=True)
    count_5 = min(9, count_5)
    if prime == (2**count_2)*(5**count_5) + 1:
        return True
    possible_exp = sorted([(2**exp2)*(5**exp5)
                           for exp2 in range(0, count_2 + 1)
                           for exp5 in range(0, count_5 + 1)])
    for exp in possible_exp:
        if (10**exp - 1) % prime == 0:
            return True
    return False

PRIMES = sieve(453377)
prime_index = 3 # 2, 3, and 5 are false positives
matches = []
while len(matches) < 40:
    prime = PRIMES[prime_index]
    if is_valid(prime):
        matches.append(prime)
    prime_index += 1

print sum(matches)
