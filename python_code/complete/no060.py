import operator

from python_code.functions import is_prime
from python_code.functions import sieve

MAX_n = 10**4
PRIMES = sieve(MAX_n)
num_primes = len(PRIMES)
partner_hash = {}
for first in range(num_primes - 1):
    prime1 = PRIMES[first]
    for second in range(first + 1, num_primes):
        prime2 = PRIMES[second]
        cand1 = int(str(prime1) + str(prime2))
        cand2 = int(str(prime2) + str(prime1))
        if is_prime(cand1, primes=PRIMES, failure_point=MAX_n**2):
            if is_prime(cand2, primes=PRIMES, failure_point=MAX_n**2):
                if prime1 in partner_hash:
                    partner_hash[prime1].append(prime2)
                else:
                    partner_hash[prime1] = [prime2]
                if prime2 in partner_hash:
                    partner_hash[prime2].append(prime1)
                else:
                    partner_hash[prime2] = [prime1]

size = 1
valid = [[prime] for prime in partner_hash]
for size in range(2, 5 + 1):
    next = []
    for subset in valid:
        could_add = partner_hash[subset[0]]
        for prime in subset:
            could_add = [p for p in could_add
                         if p in partner_hash[prime]]
        next.extend([subset[:] + [cand] for cand in could_add])
    valid = next

min_sum = 10**10
min_set = None
for subset in valid:
    if sum(subset) < min_sum:
        min_sum = sum(subset)
        min_set = subset

print min_sum, min_set
