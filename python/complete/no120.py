#!/usr/bin/env python

# (a+1)**n + (a-1)**n == na + 1 + (-1)**n(1 - na) mod a**2
# If n even, na + 1 + (1-na) = 2 mod a**2
# If n odd, (na + 1) - (1-na) = 2an mod a**2
# For a >= 3, set n = 1, then 2an > 2 and 2an < a**2 hence
# max occurs when n is odd

# Since 2an is a multiple of a, the best we can do is
# -a or -2a mod a**2

# a odd, set n = (a-1)/2 + ak (until n is odd)
# then 2an == 2ka**2 + a(a-1) == a**2 - a

# a even, set n = a/2 - 1 + ak (until n is odd)
# then 2an == 2ka**2 + a**2 - 2a == a**2 - 2a

# For even a r_m(a) = a**2 - 2*a
# For odd a r_m(a) = a**2 - a

from python.decorators import euler_timer


def main(verbose=False):
    low = 3
    high = 1000
    if low % 2 == 1:
        odds = range(low, high + 1, 2)
        evens = range(low + 1, high + 1, 2)
    else:
        odds = range(low + 1, high + 1, 2)
        evens = range(low, high + 1, 2)

    odd_sum = sum(val ** 2 - val for val in odds)
    even_sum = sum(val ** 2 - 2 * val for val in evens)
    return odd_sum + even_sum

if __name__ == '__main__':
    print euler_timer(120)(main)(verbose=True)
