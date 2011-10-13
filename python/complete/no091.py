#!/usr/bin/env python

from math import sqrt

from python.decorators import euler_timer

def forms_right_triangle(p, q):
    # squared val of sides
    squared_values = sorted([p[0]**2 + p[1]**2,
                             q[0]**2 + q[1]**2,
                             (p[0] - q[0])**2 + (p[1] - q[1])**2])
    # Get rid of identical points
    if 0 in squared_values:
        return False
    # Get rid of collinearity
    a, b, c = [sqrt(val) for val in squared_values]
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return (squared_values[0] + squared_values[1] == squared_values[2])

def main(verbose=False):
    n = 50
    result = set()
    points = [(x,y) for x in range(n + 1) for y in range(n + 1)]
    num_points = (n + 1)**2 # len(points), clearly
    # loop through all combinations of p and q
    for i in range(num_points - 1):
        for j in range(i + 1, num_points):
            p = points[i]
            q = points[j]
            if forms_right_triangle(p, q):
                result.add((p,q))
    return len(result)

if __name__ == '__main__':
    print euler_timer(91)(main)(verbose=True)
