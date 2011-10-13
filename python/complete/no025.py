#!/usr/bin/env python

# What is the first term in the Fibonacci sequence to contain 1000 digits?

from python.decorators import euler_timer
from python.functions import fibonacci_generator

def main(verbose=False):
    fib = fibonacci_generator()
    fib_index = 0
    for value in fib:
        # number of digits
        if len(str(value)) < 1000:
            fib_index += 1
            continue
        else:
            return fib_index

if __name__ == '__main__':
    print euler_timer(25)(main)(verbose=True)
