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
                # sets value to [] if not set, returns value at key
                adjacency.setdefault(node, []).append((dest, value))
                adjacency.setdefault(dest, []).append((node, value))

    _, min_sum = prims_algo(adjacency)

    return network_sum - min_sum

if __name__ == '__main__':
    print euler_timer(107)(main)(verbose=True)
