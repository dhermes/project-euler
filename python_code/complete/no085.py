#!/usr/bin/env python

# By counting carefully it can be seen that a rectangular grid measuring
# 3 by 2 contains eighteen rectangles:
# Although there exists no rectangular grid that contains exactly two
# million rectangles, find the area of the grid with the nearest solution.

# (3,2)
# T1(1,1)-->(3+1-1,2+1-1)=(3,2)=6
# T2(2,1)-->(3+1-2,2+1-1)=(2,2)=4
# T3(3,1)-->(3+1-3,2+1-1)=(1,2)=2
# B1(1,2)-->(3+1-1,2+1-2)=(3,1)=3
# B2(2,2)-->(3+1-2,2+1-2)=(2,1)=2
# B3(3,2)-->(3+1-3,2+1-2)=(1,1)=1
# (1+2+3)(1+2)

# (m,n)
# ...
# m(m+1)/2 * n(n+1)/2

# Find P = m(m+1)n(n+1) nearest to 8000000
# WLOG n <= m
# WLOG n <= m, P <= m^2(m+1)^2

# n >= 1, 2P + 1 >= 4m^2 + 4m + 1 >= 16*10**6 + 1
# m >= 1999.5

from python_code.decorators import euler_timer

def main(verbose=False):
    max_m = int(((16*10**6 + 1)**(0.5) - 1)/2.0) + 1
    closest = 0
    area = 0
    for m in range(1, max_m + 1):
        for n in range(1, m + 1):
            if abs(m*n*(m+1)*(n+1) - 8*10**6) < abs(closest - 8*10**6):
                closest = m*n*(m+1)*(n+1)
                area = m*n
    return area

if __name__ == "__main__":
    print euler_timer(85)(main)(verbose=True)
