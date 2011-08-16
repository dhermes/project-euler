#!/usr/bin/env python

# The problem is a generalization of one when n = 32
# Let E(N)_n = the expected value when the y_i, x_i
# have n bits. Then
# E(N)_n = sum_{k=0 to n} (n choose k)/(2**n) [E(N)_{n - k} + 1]
# Since k of the bits are set with probability (n choose k)/(2**n)
# Once k bits are set, they remain set forever, so our
# expected time going forward if E(N)_{n - k} + 1 since it takes
# 1 step to first set k bits and E(N)_{n - k} steps to set the
# remaining (n - k) bits

# 2**n E(N)_n = 2**n + sum_{k=0 to n} (n choose k) E(N)_{n - k}
# Reworking this, with E(N)_{n - n} = E(N)_0 = 0, we have
# (2**n - 1) E(N)_n = 2**n + sum_{k=1 to n} (n choose k) E(N)_{n - k}

from python_code.decorators import euler_timer
from python_code.functions import choose

def main(verbose=False):
    expected_hash = {0: 0}
    for n in range(1, 32 + 1):
        to_add = 2**n
        for k in range(1, n + 1):
            to_add += choose(n, k)*expected_hash[n - k]
        expected_hash[n] = (to_add*1.0)/(2**n - 1)

    return round(expected_hash[32], 10)

if __name__ == '__main__':
    print euler_timer(323)(main)(verbose=True)
