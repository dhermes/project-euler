#!/usr/bin/env python

# Write n = a_k ... a_1 a_0, then
# f(n) = (all but the last digit of n) + (the last digit of n)*m
# is equivalent to
# f(n) = (n - a_0)/10 + a_0*m = (1/10)*(n + (10*m - 1)*a_0)
# Since "p > 1 coprime to 10", we know 10 is invertible in Z_p,
# So in order for n == 0 mod p <==> f(n) == 0 mod p to hold,
# we must have 10*m - 1 == 0 mod p (the operation works independent of a_0)
# Thus m is 10**(-1) mod p

from python.decorators import euler_timer
from python.functions import sieve
from python.functions import inverse_mod_n

def main(verbose=False):
    PRIMES = sieve(10**7)
    running_sum = 0
    for prime in PRIMES:
        if prime not in [2, 5]:
            running_sum += inverse_mod_n(10, prime)
    return running_sum

if __name__ == '__main__':
    print euler_timer(274)(main)(verbose=True)
