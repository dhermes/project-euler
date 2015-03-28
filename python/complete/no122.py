#!/usr/bin/env python

from python.decorators import euler_timer


def main(verbose=False):
    MAX_n = 200

    optimal_chains = {1: [[1]]}
    for exponent in range(2, MAX_n + 1):
        addition_chains = []
        for needed_value in xrange(1, exponent / 2 + 1):
            for chain in optimal_chains[exponent - needed_value]:
                if needed_value in chain:
                    addition_chains.append(chain[:] + [exponent])

        min_length = min(len(chain) for chain in addition_chains)
        optimal_chains[exponent] = [chain for chain in addition_chains
                                    if len(chain) == min_length]

    return sum(len(chain[0]) - 1 for chain in optimal_chains.values())

if __name__ == '__main__':
    print euler_timer(122)(main)(verbose=True)
