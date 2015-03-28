#!/usr/bin/env python

# P = 28433 x 2^7830457 + 1 is a big prime number

# Find the last ten digits of this prime number.

# P mod 10**10 is relevant to us
# From CRT, we can find this in 2**10 and 5**10
# P == 1 mod 2**10 since 2**7830457 == 0

# Since 2 is a unit in integers mod 5**10, we know it has
# order dividing phi(5**10) = 4(5**9), which has 3*10 = 30 factors
# 1, 5,...,1*(5**9)
# 2,10,...,2*(5**9)
# 4,20,...,4*(5**9)

from python.decorators import euler_timer
from python.functions import order_mod_n


def unit_a_null_b(a, b):
    k = 1
    while (k * a + 1) % b != 0:
        k += 1
    return (k * a + 1) % (a * b)


def main(verbose=False):
    # We need to find the residue of P modulo 5**10
    # since we already know the residue modulo 2**10
    actual_exponent = 7830457 % order_mod_n(2, 5 ** 10)
    # want to find 2 raised to this exponent
    power_of_two = 1
    for i in range(actual_exponent):
        power_of_two = (2 * power_of_two) % 5 ** 10
    residue = (28433 * power_of_two + 1) % 5 ** 10

    unit_two_null_five = unit_a_null_b(2 ** 10, 5 ** 10)
    unit_five_null_two = unit_a_null_b(5 ** 10, 2 ** 10)
    return (1 * unit_two_null_five + residue * unit_five_null_two) % 10 ** 10

if __name__ == '__main__':
    print euler_timer(97)(main)(verbose=True)
