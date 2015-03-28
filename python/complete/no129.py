#!/usr/bin/env python

# R(k) = (10^k - 1)/9
# So the smallest k such that R(k) == 0 mod n is the order
# of the element 10 in the multiplicative group of units
# when 9 is invertible. When 9 is not invertible (i.e.
# when 3 | n), we have R(k) = f*n <==> 10**k - 1 == f*(9*n)
# hence A(n) = order of 10 modulo (9*n)

# To start at 10**6 we need to verify A(n) <= n.
# Consider R(1) mod n, R(2) mod n, ..., R(n + 1) mod n.
# By pigeonhole, there exist i < j <= n + 1 with
# R(i) mod n = R(j) mod n (since only n residues mod n)
# Thus 0 = R(j) - R(i) mod n = (10**i)*R(j - i) mod n
# Since (10, n) = 1, 10 is invertible, hence
# (10**i)*R(j - i) mod n == 0 <==> R(j - i) mod n
# But j - i <= n + 1 - i <= n since i >= 1, so
# We are guaranteed there exists some k <= n with
# R(k) <= n

from fractions import gcd

from python.decorators import euler_timer
from python.functions import order_mod_n


def main(verbose=False):
    max_a = 0
    n = 10 ** 6
    while max_a <= 10 ** 6:
        n += 1
        if gcd(10, n) == 1:
            basis = n
            if n % 3 == 0:
                basis = 9 * n
            curr_order = order_mod_n(10, basis)
            if curr_order > max_a:
                max_a = curr_order
    return n

if __name__ == '__main__':
    print euler_timer(129)(main)(verbose=True)
