#!/usr/bin/env python

from math import log

from python_code.decorators import euler_timer
from python_code.functions import get_data

def main(verbose=False):
    data = [row.split(",") for row in get_data(99).split("\n") if row]

    max_val = -1
    winner = None
    for i, row in enumerate(data):
        log_val = int(row[1])*log(int(row[0]))
        if log_val > max_val:
            max_val = log_val
            winner = i

    return winner + 1 # account for 0 vs. 1 initial index

if __name__ == "__main__":
    print euler_timer(99)(main)(verbose=True)
