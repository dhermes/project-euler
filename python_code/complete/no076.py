#!/usr/bin/env python

# It is possible to write five as a sum in exactly six different ways:

# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1

# How many different ways can one hundred be written as a sum of at least
# two positive integers?

#################################
# p(k, n) - represents the number of partitions of n using only natural
# numbers at least as large as k

# p(n) = 1 + sum_{k = 1}^{floor(n/2)} p(k, n - k)

# p(k, n) = 0 if k > n
# p(k, n) = 1 if k = n
# p(k, n) = p(k + 1, n) + p(k, n - k) otherwise

# Our final is p(1, n)

from python_code.decorators import euler_timer

def partitions(n):
    from math import sqrt
    p = {}
    for k in range(1, n + 1):
        p[(k, k)] = 1
        for i in range(k - 1, 0, -1):
            if i > k - i:
                p[(i, k)] = p[(i + 1, k)]
            else:
                p[(i, k)] = p[(i + 1, k)] + p[(i, k - i)]
    return p[(1, n)]

def main(verbose=False):
    return partitions(100) - 1

if __name__ == "__main__":
    print euler_timer(76)(main)(verbose=True)
