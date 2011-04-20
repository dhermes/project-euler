from python_code.functions import prime_factors
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

PRIMES = sieve(10**6 + 3) # 10**6 + 3 is the final value of p_2

running_sum = 0
for index in range(2, len(PRIMES) - 1):
    p_1 = PRIMES[index]
    p_2 = PRIMES[index + 1]
    _, ten_inverse = extended_euclid(p_2, 10)
    digits = len(str(p_1))
    k = (ten_inverse**digits)*(p_2 - p_1) % p_2
    running_sum += int('%s%s' % (k, p_1))
print running_sum
