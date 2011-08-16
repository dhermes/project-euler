#!/usr/bin/env python

from python_code.decorators import euler_timer
from python_code.functions import get_data

def column_by_column(data):
    result = {}
    size = len(data)
    # First column is set
    for row in range(size):
        result[(row, 0)] = data[row][0]

    for column in range(1, size):
        for row in range(size):
            set_val = result[(row, column - 1)] + data[row][column]
            for under in range(row):
                val = result[(under, column - 1)] + \
                      sum([data[ind][column] for ind in range(under, row + 1)])
                if val < set_val:
                    set_val = val
            for over in range(row + 1, size):
                val = result[(over, column - 1)] + \
                      sum([data[ind][column] for ind in range(row, over + 1)])
                if val < set_val:
                    set_val = val
            result[(row, column)] = set_val

    return min([result[(row, size - 1)] for row in range(size)])

def main(verbose=False):
    data = [[int(entry) for entry in row.split(",")]
            for row in get_data(82).split("\n") if row]

    return column_by_column(data)

if __name__ == '__main__':
    print euler_timer(82)(main)(verbose=True)
