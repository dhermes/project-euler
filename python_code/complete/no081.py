#!/usr/bin/env python

from python_code.decorators import euler_timer
from python_code.functions import astar
from python_code.functions import get_data

def main(verbose=False):
    data = [[int(entry) for entry in row.split(",")]
            for row in get_data(81).split("\n") if row]

    arranged_data = {}
    size = len(data)
    for i in range(size):
        for j in range(size):
            arranged_data[(i, j)] = data[i][j]

    MINIMUM = min(arranged_data.values())
    def heuristic(node):
        return (2*size - 2 - sum(node))*MINIMUM

    def adjacent(node):
        node_x, node_y = node
        return [(node_x + 1, node_y), (node_x, node_y + 1)]

    return astar(arranged_data,
                 (0, 0),
                 (size - 1, size - 1),
                 heuristic,
                 adjacent)

if __name__ == "__main__":
    print euler_timer(81)(main)(verbose=True)

