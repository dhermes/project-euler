#!/usr/bin/env python

from math import sqrt

from python.decorators import euler_timer

def inner_circle(e1, e2, e3):
    # Using (e1 + e2 + e3 + e4)^2 = 2(e1^2 + e2^2 + e3^2 + e4^2)
    # A = e1^2 + e2^2 + e3^2; B = e1 + e2 + e3
    # We have e4 = B +/- sqrt(2(B^2 - A))
    # inner circle will have smaller radii, hence
    # larger eccentricity, so we set e4 = B + sqrt(...)
    from math import sqrt

    A = e1**2 + e2**2 + e3**2
    B = e1 + e2 + e3
    return B + sqrt(2*(B**2 - A))

def next_3(node):
    points, eccentricity = node
    e1, e2, e3 = points
    return [[(eccentricity, e1, e2), inner_circle(eccentricity, e1, e2)],
            [(eccentricity, e2, e3), inner_circle(eccentricity, e2, e3)],
            [(eccentricity, e3, e1), inner_circle(eccentricity, e3, e1)]]

def main(verbose=False):
    iterations = 10
    C = {}
    C[-1] = {0: [(1,1,1), 3 - 2*sqrt(3)] }
    C[0] = {0: [(1, 1, 3 - 2*sqrt(3)), 1],
            1: [(1, 1, 3 - 2*sqrt(3)), 1],
            2: [(1, 1, 3 - 2*sqrt(3)), 1]}
    C[1] = {}
    first_level = inner_circle(1, 1, 3 - 2*sqrt(3))
    for i in range(3):
        C[1][i] = [(3 - 2*sqrt(3), 1, 1), first_level]
    C[1][3] = [(1, 1, 1), inner_circle(1, 1, 1)]
    for i in range(2, iterations + 1):
        C[i] = {}
        for node, value in C[i - 1].items():
            n1, n2, n3 = next_3(value)
            C[i][3*node] = n1
            C[i][3*node + 1] = n2
            C[i][3*node + 2] = n3

    total_area = (1.0/C[-1][0][1])**2
    covered_area = 0
    for i in range(iterations + 1):
        for j in C[i]:
            covered_area += (1.0/C[i][j][1])**2

    return round(1-covered_area/total_area, 8)

if __name__ == '__main__':
    print euler_timer(199)(main)(verbose=True)
