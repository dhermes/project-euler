#!/usr/bin/env python

# p_1^2 + p_2^3 + p_3^4 = n

from python_code.decorators import euler_timer
from python_code.functions import all_factors

def nontrivial_factorizations(n):
    factor_hash = {1: [1]}
    factor_hash = all_factors(n, factor_hash)
    result = {1: [[]], 2: [[2]]}
    value_hash = {}
    for i in range(3, n + 1):
        to_add = [[i]]
        for factor in factor_hash[i]:
            if factor > 1 and factor**2 <= i:
                for subset1 in result[factor]:
                    for subset2 in result[i/factor]:
                        cand = sorted(subset1 + subset2)
                        if cand not in to_add:
                            to_add.append(cand)
        for match in to_add:
            new_k = i + len(match) - sum(match)
            if new_k > 1 and new_k not in value_hash:
                value_hash[new_k] = i
        result[i] = to_add
    return result, value_hash


def main(verbose=False):
    MAX_k = 12000
    MAX_n = MAX_k + 1000
    _, value_hash = nontrivial_factorizations(MAX_n)
    final_list = []
    for desired in range(2, MAX_k + 1):
        if desired not in value_hash:
            raise Exception("Subset not large enough, raise MAX_n.")
        if value_hash[desired] not in final_list:
            final_list.append(value_hash[desired])
    return sum(final_list)

if __name__ == "__main__":
    print euler_timer(88)(main)(verbose=True)
