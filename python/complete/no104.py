#!/usr/bin/env python

from math import exp
from math import log
from math import sqrt

from python.decorators import euler_timer

def is_1_9_pandigital(n):
    digs = [int(dig) for dig in str(n)]
    if len(digs) != 9:
        return False
    return sorted(digs) == range(1, 10)

def log_fib(n):
    root_plus = 0.5*(1 + sqrt(5))
    root_ratio = 0.5*(sqrt(5) - 3)
    return n*log(root_plus) - 0.5*log(5) + log(1 - root_ratio**n)

def main(verbose=False):
    # 10**(d - 1) <= N < 10**d
    # d <= log(N)/log(10) + 1 < d + 1
    k = 2
    a, b = 1, 1
    solution_found = False
    while not solution_found:
        if is_1_9_pandigital(b):
            log_val = log_fib(k)
            digits = int(log_val/log(10) + 1)
            log_last_9 = log_val - (digits - 9)*log(10)
            last_9 = int(exp(log_last_9))
            if is_1_9_pandigital(last_9):
                solution_found = True
        a, b = b, (a + b) % (10**9)
        if not solution_found:
            k += 1
    return k

if __name__ == '__main__':
    print euler_timer(104)(main)(verbose=True)
