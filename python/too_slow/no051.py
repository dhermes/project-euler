#!/usr/bin/env python

from python.decorators import euler_timer
from python.functions import sieve

def most_common_digit(n):
    digs = set(str(n))
    counts = [(dig, str(n).count(dig)) for dig in digs]
    return sorted(counts, key=lambda pair: pair[1])[-1]

def find_and_replace(n, dig):
    digits = range(10)
    if str(n)[0] == dig:
        digits.remove(0) # no leading 0s

    string_val = str(n)
    result = [string_val.replace(dig, str(substitute))
              for substitute in digits]
    return [int(val) for val in result]

def main(verbose=False):
    PRIMES = sieve(10**6)

    for prime in PRIMES:
        digit, count = most_common_digit(prime)
        if count > 2:
            candidates = find_and_replace(prime, digit)
            match_count = 0
            for candidate in candidates:
                if candidate in PRIMES:
                    match_count += 1
            if match_count == 8:
                return prime

if __name__ == '__main__':
    print euler_timer(51)(main)(verbose=True)
