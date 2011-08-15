#!/usr/bin/env python

from python_code.decorators import euler_timer
from python_code.functions import fill_count

def main(verbose=False):
    return fill_count(3, 50)

if __name__ == "__main__":
    print euler_timer(114)(main)(verbose=True)
