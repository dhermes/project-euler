#!/usr/bin/env python

# In England there are 8 coins in circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, 100p and 200p.
# How many different ways can 200p be made using any number of coins?

# This will be the coeficient of x^200 in
# (1 + x + x^2 + ...)(1 + x^2 + x^4 + ...)(1 + x^5 + x^10 + ...)*...
# ...*(1 + x^10 + x^20 + ...)(1 + x^20 + x^40 + ...)(1 + x^50 + x^100 + ...)

from python.decorators import euler_timer

def polynomial_add(left, right):
    max_len = max(len(left), len(right))
    to_add_left = [0]*(max_len - len(left)) + left[:]
    to_add_right = [0]*(max_len - len(right)) + right[:]
    return [to_add_left[i] + to_add_right[i] for i in range(max_len)]

# represent ax^n + bx^(n-1) + ... + c as [c,...b,a]
# 1 + 2x + x^2 + 2x^3 = (1+2x)*(1+x^2) =
# [1,2]*[1,0,1] = [1,0,1,0] + [2,0,2] = [1,2,1,2]
def polynomial_mult(f, g):
    result = []
    for ind in range(len(f)):
        to_add = [f[-ind - 1]*coeff for coeff in g] + [0] * ind
        result = polynomial_add(result, to_add)
    return result

def generating_poly(max_power, base):
    add_on = [0]*(base - 1) + [1]
    return [1] + add_on * (max_power/base)

def main(verbose=False):
    prod = generating_poly(200,1)
    coins = [2, 5, 10, 20, 50, 100, 200]
    for coin in coins:
        prod = polynomial_mult(prod, generating_poly(200,coin))
    return prod[200]

if __name__ == '__main__':
    print euler_timer(31)(main)(verbose=True)
