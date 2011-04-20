from python_code.decorators import euler_timer
from python_code.functions import all_factors
from python_code.functions import first_prime_divisor
from python_code.functions import robust_divide
from python_code.functions import sieve

n = 10**6
PRIMES = sieve(n)

def sum_factors(n, hash_={}, primes=[]):
    if n in hash_:
        return hash_[n]
    elif n == 1:
        hash_[1] = 1
        return 1
    if primes == []:
        primes = sieve(n)

    prime, _  = first_prime_divisor(n, primes)
    quotient, count = robust_divide(n, prime, include_count=True)
    factor = (prime**(count + 1) - 1)/(prime - 1)
    hash_[n] = factor*sum_factors(quotient, hash_=hash_, primes=primes)
    return hash_[n]

def amicable_cycle(n, cycle_hash, factor_sum_hash, primes, break_point):
    if n in cycle_hash:
        return cycle_hash[n][1]

    cycle = [n]
    next = sum_factors(n, factor_sum_hash, primes) - n
    while (next not in cycle_hash and
           next not in cycle and
           next <= break_point):
        cycle.append(next)
        next = sum_factors(next, factor_sum_hash, primes) - next

    if next > break_point:
        set_val = [None]
    elif next in cycle_hash:
        set_val = cycle_hash[next][1]
    elif next in cycle:
        start = cycle.index(next)
        set_val = cycle[start:]
    else:
        raise Exception("Shouldn't happen")
    for val in cycle:
        cycle_hash[val] = (factor_sum_hash[val] - val, set_val[:])
    return cycle_hash[n][1]

chains = {1: (0, [0]),
          2: (1, [0]),
          3: (1, [0])}

h = {1: 1,
     2: 3,
     3: 4}

for i in range(4, n + 1):
    amicable_cycle(i, chains, h, PRIMES, 10**6 + 1)

best_length = 0
longest_chain = None
for i in range(1, n + 1):
    chain = chains[i][1]
    if len(chain) > best_length:
        best_length = len(chain)
        longest_chain = chain[:]

print min(longest_chain)
