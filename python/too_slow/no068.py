#!/usr/bin/env python

# a0
#              a1
#        a2
#    a3      a4
# a5
#      a6  a7  a8
#        a9

# In clockwise order, chains are
# (a0, a2, a4)
# (a1, a4, a7)
# (a8, a7, a6)
# (a9, a6, a3)
# (a5, a3, a2)

from python.decorators import euler_timer
from python.functions import all_permutations

def magic_5_gon(perm):
    node_indices = [0, 1, 8, 9, 5]
    triples = {0: [0, 2, 4],
               1: [1, 4, 7],
               8: [8, 7, 6],
               9: [9, 6, 3],
               5: [5, 3, 2]}
    node_values = [perm[ind] for ind in node_indices]
    start = node_values.index(min(node_values))

    ordered_nodes = node_indices[start:] + node_indices[:start]
    result = []
    for node in ordered_nodes:
        curr_ind = triples[node]
        result.append([perm[ind] for ind in curr_ind])
    return result

def main(verbose=False):
    result = []
    perms = all_permutations(range(1,11))
    for perm in perms:
        magic = magic_5_gon(perm)
        sums = [sum(triple) for triple in magic]
        if len(set(sums)) == 1:
            to_add = "".join("".join(str(ind) for ind in triple)
                             for triple in magic)
            result.append(to_add)
    return max(int(concat) for concat in result if len(concat) == 16)

if __name__ == '__main__':
    print euler_timer(68)(main)(verbose=True)
