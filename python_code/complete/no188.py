#!/usr/bin/env python

# Define the operator {{ as such:
# a {{ 1 = a,
# a {{ (k + 1) = a**(a {{ k)

# Find the last 8 digits of 1777 {{ 1855.

# E.G. 2 {{ 4 = 2**(2 {{ 3) = 2**(2**(2 {{ 2))
# = 2**(2**(2**(2))) = 2**16 = 65536

####################
# Let Y = ord_X(a) be the order of a mod X, then
# a**n == a**(n mod Y) mod X
# if n = a**b, then
# n mod Y == a**b mod Y = a**(b mod ord_Y(a)) mod Y

# So we have
# a**(a**a) mod X = f(a, 3, X) = a**f(a, 2, ord_X(a))
# f(a, k, X) = a**f(a, k - 1, ord_X(a))
# With boundary conditions
# f(a, 1, X) = a % X
# f(a, k, 1) = 1
# f(a, k, 2) = a % 2 (since a**P == a mod 2 for all P > 1)

from python_code.decorators import euler_timer
from python_code.functions import order_mod_n

def hyper_exponentiate(a, b, modulus):
    if modulus == 1:
        return 1
    elif modulus == 2:
        return a % 2
    if b == 1:
        return a % modulus
    a_order = order_mod_n(a, modulus)
    return (a**hyper_exponentiate(a, b - 1, a_order)) % modulus

def main(verbose=False):
    return hyper_exponentiate(1777, 1855, 10**8)

if __name__ == '__main__':
    print euler_timer(188)(main)(verbose=True)
