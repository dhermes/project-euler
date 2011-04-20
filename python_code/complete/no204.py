import operator
from itertools import product as i_product
from math import floor
from math import log

from python_code.functions import sieve

def hamming_type(max_n, primes):
    # assumes primes is sorted
    if primes == []:
        return 1

    count = 0
    prime = primes[0]
    max_power = int(floor(log(max_n)/log(prime)))
    for power in range(max_power + 1):
        count += hamming_type(max_n/(prime**power), primes[1:])
    return count

PRIMES = sieve(100)
print hamming_type(10**9, PRIMES)
