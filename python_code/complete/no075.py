#!/usr/bin/env python

# It turns out that 12 cm is the smallest length of wire that can be
# bent to form an integer sided right angle triangle in exactly one
# way, but there are many more examples.

# 12 cm: (3,4,5)
# 24 cm: (6,8,10)
# 30 cm: (5,12,13)
# 36 cm: (9,12,15)
# 40 cm: (8,15,17)
# 48 cm: (12,16,20)

# In contrast, some lengths of wire, like 20 cm, cannot be bent to form
# an integer sided right angle triangle, and other lengths allow more
# than one solution to be found; for example, using 120 cm it is possible
# to form exactly three different integer sided right angle triangles.

# 120 cm: (30,40,50), (20,48,52), (24,45,51)

# Given that L is the length of the wire, for how many values of L <= 1,500,000
# can exactly one integer sided right angle triangle be formed?

################################

# All pythagorean triples can be represented:
# k(m**2 - n**2), k*(2*m*n), k(m**2 + n**2)
# With m > n and (m, n) == 1
# Hence L = 2*k*m*(m + n)

# m*(m + n) = L/(2k), m > n > 0 requires
# m**2 < m*(m + n) < L/(2k)

# Letting k = 1 gives a primitive solution

# If m is even, then n must be odd, but
# if m is odd, n may be odd as well and
# (n, m) == 1 can still be satisfied

# However, consider a primitive triple
# (a, b, c). If both a and b are even,
# then 2 | (a, b), which contradicts
# primitive. If both a and b are odd,
# then c**2 == a**2 + b**2 == 2 mod 4,
# which is impossible. Hence WLOG
# a is odd and b is even.

# Applying this to (m, n), the triple
# (m**2 - n**2, 2*m*n, m**2 + n**2)
# we have 2*m*n even, hence b = 2*m*n
# and we need m**2 - n**2 = a to be
# odd, else the triple is not primitive.
# Hence m and n need opposite parity.

from fractions import gcd
from math import sqrt

from python_code.decorators import euler_timer

def main(verbose=False):
    MAX_n = 1500000
    number_solutions = {}

    max_m = int(sqrt(0.5*MAX_n))
    for m in xrange(2, max_m + 1):
        # m, n need opposite parity
        n_parity = 0 if m % 2 else 1
        for n in xrange(n_parity, m, 2):
            if gcd(m, n) == 1:
                primitive = 2*m*(m + n)
                # m is fixed, so as n
                # increases, primitive will
                # and we break the inner loop when
                # it exceeds the MAX_n
                if primitive > MAX_n:
                    break
                # Once we have the perimeter of
                # the primitive triangle, we also
                # have 2*perimiter, 3*perimeter, 4*perimeter, etc.
                for perimeter in range(primitive, MAX_n + 1, primitive):
                    if perimeter in number_solutions:
                        number_solutions[perimeter] += 1
                    else:
                        number_solutions[perimeter] = 1

    return len([val for val in number_solutions.values() if val == 1])

if __name__ == '__main__':
    print euler_timer(75)(main)(verbose=True)
