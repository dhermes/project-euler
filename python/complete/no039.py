#!/usr/bin/env python

# For p, we seek k, m, n > 0 such that n < m and 2*k*m*(m + n) = p

from python.decorators import euler_timer
from python.functions import all_factors


def all_triples(p, factors_hash=None):
    if factors_hash is None:
        factors_hash = {}

    if p % 2 == 1 or p < 2 or not isinstance(p, int):
        return []

    if p / 2 in factors_hash:
        choices_k = factors_hash[p / 2]
    else:
        choices_k = all_factors(p / 2, factors_hash)[p / 2]

    result = []
    for k in choices_k:
        if p / (2 * k) in factors_hash:
            choices_m = factors_hash[p / (2 * k)]
        else:
            choices_m = all_factors(p / (2 * k), factors_hash)[p / (2 * k)]

        # 2*k*m*(m + n) = p
        for m in choices_m:
            n = p / (2 * k * m) - m
            if n > 0 and m > n:
                result.append((k, m, n))

    return result


def convert_to_triangle(triple):
    k, m, n = triple
    a = k * (m ** 2 - n ** 2)
    b = k * (2 * m * n)
    c = k * (m ** 2 + n ** 2)
    return tuple(sorted((a, b, c)))


def all_triangles(p, factors_hash=None):
    triples = all_triples(p, factors_hash)
    return list(set(convert_to_triangle(triple) for triple in triples))


def all_triangles_up_to_n(n):
    factors_hash = all_factors(n)
    result = {}
    for p in range(2, n + 1, 2):
        result[p] = all_triangles(p, factors_hash)
    return result


def main(verbose=False):
    all_tri = all_triangles_up_to_n(1000)
    lengths = {}
    max_val = -1
    max_keys = []
    for key, value in all_tri.iteritems():
        curr_length = len(value)
        if curr_length > max_val:
            max_keys = [key]
            max_val = curr_length
        elif curr_length == max_val:
            max_keys.append(key)

    if len(max_keys) != 1:
        raise("Keys are not unique")

    return max_keys[0]

if __name__ == '__main__':
    print euler_timer(39)(main)(verbose=True)
