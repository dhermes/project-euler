#!/usr/bin/env python

from python.decorators import euler_timer
from python.functions import inverse_mod_n
from python.functions import sieve

def main(verbose=False):
    PRIMES = sieve(10**6 + 3) # 10**6 + 3 is the final value of p_2

    running_sum = 0
    for index in range(2, len(PRIMES) - 1):
        p_1 = PRIMES[index]
        p_2 = PRIMES[index + 1]
        ten_inverse = inverse_mod_n(10, p_2)
        digits = len(str(p_1))
        k = (ten_inverse**digits)*(p_2 - p_1) % p_2
        running_sum += int('%s%s' % (k, p_1))
    return running_sum

if __name__ == '__main__':
    print euler_timer(134)(main)(verbose=True)
