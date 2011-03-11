from os import path as opath
import sys
from math import sqrt
from fractions import gcd

############################################################
##################### HELPER FUNCTIONS #####################
############################################################

# 8, 11, 13, 18, 22, 42, 54, 59, 67
def get_data(problem_number):
    """
    Takes a problem number and returns the raw text
    from the expected data file

    Data is expected to be in euler_project/problem_data and
    to be named no---.txt where --- is the zero padded
    problem number
    """
    path = opath.abspath(opath.dirname(sys.argv[0]))

    relative_filename = 'no%s.txt' % str(problem_number).zfill(3)
    relative_path = "/".join(["..",
                              "..",
                              "problem_data",
                              relative_filename])

    filename = opath.join(path, relative_path)
    with open(filename) as fh:
        # fails if file doesn't exist
        result = fh.read()
    return result

# 26
def robust_divide(n, quotient, include_count=False):
    if quotient in (-1, 1):
        raise ValueError("Please don't use %s as a quotient." % quotient)

    result = n
    count = 0
    while result % quotient == 0:
        count += 1
        result = result/quotient
    if include_count:
        return result, count
    else:
        return result

############################################################
##################### PROBLEM SPECIFIC #####################
############################################################

# 18, 67
def max_sum(triangle_matrix):
    """
    Finds maximum sum of path from top of triangle down to bottom

    Input: Matrix of triangle e.g.
      1
     3 5
    7 8 4
    becomes [[1], [3, 5], [7, 8, 4]]
    Uses memoization from the bottom layer up to work quickly
    Output: maximum value
    """
    max_depth = len(triangle_matrix) - 1

    # Set bottom row for memoization
    depth = max_depth
    result = {}
    for i, entry in enumerate(triangle_matrix[depth]):
        result[(i, max_depth - depth)] = entry
    depth -= 1

    # Set each row moving up the triangle based on
    # the results one low below
    while depth >= 0:
        for i, entry in enumerate(triangle_matrix[depth]):
            result[(i, max_depth - depth)] = entry + max(
                result[(i, max_depth - depth - 1)], result[(i + 1, max_depth - depth - 1)] )
        depth -= 1

    return result[(0, max_depth - depth - 1)]

############################################################
######################### FIBONACCI ########################
############################################################

# 25
def fibonacci_generator():
    """a generator for Fibonacci numbers"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

############################################################
########################## PRIMES ##########################
############################################################

# 12
def first_prime_divisor(n, prime_list=None):
    if n == 1:
        return [1, 1]

    if prime_list is not None:
        for p in prime_list:
            if not n % p:
                return [p, n/p]
        raise ValueError("No prime in %s divides %s." % (prime_list, n))
    else:
        divisor = 2
        while n % divisor != 0:
            divisor += 1
        return [ divisor, n/divisor ]
    raise ValueError("Bad input %s." % n)

# 3, 12
def prime_factors(n, unique=False, hash_=None):
    if n == 1:
        return []
    if type(hash_) == dict and n in hash_:
        return hash_[n]

    prime, quotient = first_prime_divisor(n)

    remaining, count = robust_divide(n, prime, include_count=True)
    if unique:
        result = [prime] + prime_factors(remaining, unique)
    else:
        result = [prime] * count + prime_factors(remaining, unique)

    if type(hash_) == dict:
        hash_[n] = result

    return result

# 21, 23, 39
def all_factors(n, hash_ = {1:[1], 2:[1,2], 3:[1,3]}):
    """
    Takes n and optional hash of factors

    Uses the hash to update a full list of factors for
    all integers 1 to n. Only updates if not in hash_.
    """
    factor_hash = hash_.copy()
    if n in factor_hash:
        return factor_hash

    all_primes = sieve(n)

    for i in range(4,n+1):
        if i not in factor_hash:
            reduced = first_prime_divisor(i, all_primes)

            to_add = factor_hash[reduced[1]][:]
            to_add.extend([ reduced[0] * elt for elt in to_add ])
            to_add = sorted(list(set(to_add)))

            factor_hash[i] = to_add

    return factor_hash

# 7, 37
def is_prime(n):
    if n < 10:
        if n == 2 or n == 3 or n == 5 or n == 7:
            return True
        else:
            return False

    # We safely assume n >= 10
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False

    divisor_bound = int(sqrt(n))
    # From here, we know only +/- 1 mod 6 works, so
    # we start with 11 and 13
    divisor_minus, divisor_plus = 11, 13
    while divisor_minus <= divisor_bound:
        if n % divisor_minus == 0 or n % divisor_plus == 0:
            return False
        divisor_minus += 6
        divisor_plus += 6
    return True

# 10, 21, 27, 35, 37
def sieve(n):
    """
    Sieve of Eratosthenes

    Returns all primes <= n
    """
    to_check = [1] * (n+1)
    for i in range(2,n+1):
        if to_check[i]:
            for j in range(2*i,n+1,i):
                to_check[j] = 0

    return [ i for i in range(2,n+1) if to_check[i] ]

############################################################
####################### NUMBER THEORY ######################
############################################################

def order_mod_n(value, n):
    if gcd(value, n) != 1 or n == 1:
        raise ValueError("%s is not a unit modulo %s." % (value, n))
    base_residue = value % n
    if base_residue < 0:
        base_residue = base_residue + n

    residue = base_residue
    exponent = 1
    while residue != 1:
        residue = (residue * base_residue) % n
        exponent += 1
    return exponent

############################################################
###################### LIST MANAGEMENT #####################
############################################################

# 4, 23, 29
def apply_to_list(func, list_):
    result = []
    for elt1 in list_:
        for elt2 in list_:
            result.append(func(elt1, elt2))
    return result
