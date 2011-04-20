from python_code.functions import sieve

def extended_euclid(a, b):
    M = max(a, b)
    m = min(a, b)

    last = (M, [1, 0])
    curr = (m, [0, 1])
    while curr[0] > 1:
        next = last[0] % curr[0]
        factor = (last[0] - next)/curr[0]
        last, curr = curr, (next, [last[1][0] - factor*curr[1][0], last[1][1] - factor*curr[1][1]])
    result = curr[1]
    if a*result[0] + b*result[1] == 1:
        return result
    else:
        return result[::-1]

PRIMES = sieve(10**7)
running_sum = 0
for prime in PRIMES:
    if prime not in [2, 5]:
        _, m = extended_euclid(prime, 10)
        m = m % prime
        running_sum += m
print running_sum
