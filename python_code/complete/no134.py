from python_code.functions import inverse_mod_n
from python_code.functions import prime_factors
from python_code.functions import sieve

PRIMES = sieve(10**6 + 3) # 10**6 + 3 is the final value of p_2

running_sum = 0
for index in range(2, len(PRIMES) - 1):
    p_1 = PRIMES[index]
    p_2 = PRIMES[index + 1]
    ten_inverse = inverse_mod_n(10, p_2)
    digits = len(str(p_1))
    k = (ten_inverse**digits)*(p_2 - p_1) % p_2
    running_sum += int('%s%s' % (k, p_1))
print running_sum
