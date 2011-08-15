#!/usr/bin/env python

# All square roots are periodic when written as continued fractions
# and can be written in the form:

# sqrt(N) = a0 + 1/(a_1 + 1(a_2 + ...))

# For example, let us consider 23:
# sqrt(23) = 4 + sqrt(23) - 4
# = 4 + 1/(1/(sqrt(23)-4)) = 4 + 1/(1 + (sqrt(23) - 3)/7)

# If we continue we would get the following expansion:
# sqrt(23) = 4 + 1/(1 + 1/(3 + 1/(1 + 1/(8 + ...))))

# The process can be summarised as follows:
# a_0 = 4 --> 1 + (sqrt(23) - 3)/7
# a_1 = 1 --> 3 + (sqrt(23) - 3)/2
# a_2 = 3 --> 1 + (sqrt(23) - 4)/7
# a_3 = 1 --> 8 + (sqrt(23) - 4)/1
# a_4 = 8 --> 1 + (sqrt(23) - 3)/7
# a_5 = 1 --> 3 + (sqrt(23) - 3)/2
# a_6 = 3 --> 1 + (sqrt(23) - 4)/7
# a_7 = 1 --> 8 + (sqrt(23) - 4)/1

# It can be seen that the sequence is repeating. For conciseness, we use
# the notation 23 = [4;(1,3,1,8)], to indicate that the
# block (1,3,1,8) repeats indefinitely.

# The first ten continued fraction representations of
# (irrational) square roots are:

# 2=[1;(2)], period=1
# 3 =[1;(1,2)], period=2
# 5=[2;(4)], period=1
# 6=[2;(2,4)], period=2
# 7=[2;(1,1,1,4)], period=4
# 8=[2;(1,4)], period=2
# 10=[3;(6)], period=1
# 11=[3;(3,6)], period=2
# 12= [3;(2,6)], period=2
# 13=[3;(1,1,1,1,6)], period=5

# Exactly four continued fractions, for N <= 13, have an odd period.

# How many continued fractions for N <= 10000 have an odd period?

# NOTE
# We can define the following sequence to help us

# Let r_i = 1/(a_(i+1) + 1/(a(i+2) + ...
# Then 1/r_i = a_(i+1) + r_(i+1); a_i = floor(1/r_i)

# We see we can write r_i = (A_i*rt(n) + B_i)/C_i
# then 1/r_i = C_i(A_i*rt(n) - B_i)/(n*A_i**2 - B_i**2)

# represent each r_i as r_i = (A, B, C) -> 1/r_i = a + r_(i + 1)
# -> a = floor(1/r_i) = floor(C/(A rt(n) + B))
# -> r_(i + 1) = (C*A, C*B - a*(n*A**2 - B**2), n*A**2 - B**2)
# -> r_(i + 1) = (A', B', C') #reduce
# then r_(i+1) = (C_i*A_i*rt(n) - [C_i*B_i + a_(i+1)*(n*A_i**2 - B_i**2)])
#                 divided by (n*A_i**2 - B_i**2)

from python_code.decorators import euler_timer
from python_code.functions import continued_fraction_cycle
from python_code.functions import is_power

def main(verbose=False):
    non_squares = [num for num in range(1, 10000 + 1)
                   if not is_power(num, 2)]
    cycle_lengths = [len(continued_fraction_cycle(num)) - 1
                     for num in non_squares]
    return len([num for num in cycle_lengths if num % 2 == 1])

if __name__ == "__main__":
    print euler_timer(64)(main)(verbose=True)
