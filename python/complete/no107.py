#!/usr/bin/env python

from python.decorators import euler_timer
from python.functions import get_data
from python.functions import prims_algo

def main(verbose=False):
    data = [row.split(',') for row in get_data(107).split('\r\n') if row]

    adjacency = {}
    size = len(data)
    network_sum = 0
    # UNDIRECTED
    for node in range(size - 1):
        for dest in range(node + 1, size):
            if data[node][dest] != '-':
                value = int(data[node][dest])
                network_sum += value
                if node in adjacency:
                    adjacency[node].append((dest, value))
                else:
                    adjacency[node] = [(dest, value)]
                if dest in adjacency:
                    adjacency[dest].append((node, value))
                else:
                    adjacency[dest] = [(node, value)]

    _, min_sum = prims_algo(adjacency)

    return network_sum - min_sum

if __name__ == '__main__':
    print euler_timer(107)(main)(verbose=True)
