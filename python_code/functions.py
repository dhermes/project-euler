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

# 2, 57, 65
def recurrence_next(relation, values):
    """
    Assumes recurrence of length k satisfies
    f(n+k) = relation[0]*f(n) + relation[1]*f(n+1) + ...

    Values are also expected to be ordered [f(n),f(n+1),...]
    """
    if len(relation) != len(values):
        raise ValueError("Poorly specified recurrence")
    recurrence_order = len(relation)
    next_val = sum([relation[i]*values[i] for i in range(recurrence_order)])
    return values[1:] + [next_val] # copies values (doesn't change inputs)

# 4, 36, 55
def is_palindrome(n):
    return (str(n) == str(n)[::-1])

# 46
def is_power(n, exponent):
    return n == (int(n**(1.0/exponent)))**exponent

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
            val_left = result[(i, max_depth - depth - 1)]
            val_right = result[(i + 1, max_depth - depth - 1)]
            result[(i, max_depth - depth)] = entry + max(val_left, val_right)
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

def first_prime_divisor(n, prime_list=[]):
    if n == 1:
        return [1, 1]

    if prime_list != []:
        for p in prime_list:
            if n % p == 0:
                return [p, n/p]
        # To complete this loop, either the prime list was
        # insufficient or p is prime
        if is_prime(n, primes=prime_list):
            return [n, 1]
        else:
            raise ValueError("Prime list poorly specified")
    else:
        divisor = 2
        while n % divisor != 0:
            divisor += 1
        return [divisor, n/divisor]
    raise ValueError("Bad input %s." % n)

# 3, 12, 47
def prime_factors(n, unique=False, hash_=None):
    if n == 1:
        hash_[1] = []
        return []
    if type(hash_) == dict and n in hash_:
        return hash_[n]

    prime, quotient = first_prime_divisor(n)

    remaining, count = robust_divide(n, prime, include_count=True)
    if unique:
        result = [prime] + prime_factors(remaining,
                                         unique=unique,
                                         hash_=hash_)
    else:
        result = [prime] * count + prime_factors(remaining,
                                                 unique=unique,
                                                 hash_=hash_)

    if type(hash_) == dict:
        hash_[n] = result

    return result

# 135
def factors(n, factor_hash={}, primes=[]):
    if n in factor_hash:
        return factor_hash[n]
    elif n == 1:
        factor_hash[1] = [1]
        return [1]
    elif n in primes:
        factor_hash[n] = [1, n]
        return [1,n]

    prime, quotient = first_prime_divisor(n, prime_list=primes)

    to_add = factors(quotient, factor_hash, primes)[:] # Need a deep-ish copy
    to_add.extend([ prime*factor for factor in to_add ])

    factor_hash[n] = sorted(list(set(to_add)))
    return factor_hash[n]

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
            # This will update factor hash
            factors(i, factor_hash=factor_hash, primes=all_primes)

    return factor_hash

# 37, 41, 58
def is_prime(n, primes=[], failure_point=None):
    if n < 10:
        if n == 2 or n == 3 or n == 5 or n == 7:
            return True
        else:
            return False

    # We safely assume n >= 10
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False

    if failure_point is not None:
        if n >= failure_point:
            raise ValueError("%s is too large for is_prime." % n)

    if primes != []:
        if n in primes:
            return True
        to_check = [prime for prime in primes if prime**2 <= n]
        for prime in to_check:
            if n % prime == 0:
                return False
        return True

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

# 7, 10, 21, 27, 35, 37, 46, 49, 50, 51, 58, 60
def sieve(n):
    """
    Sieve of Eratosthenes

    Returns all primes <= n
    """
    to_check = [True] * (n + 1)
    final_check = int(sqrt(n)) # effectively the floor of sqrt(n)

    for i in xrange(2, final_check + 1):
        if to_check[i]:
            for j in xrange(i**2, n + 1, i):
                to_check[j] = False

    return [i for i in range(2, n + 1) if to_check[i]]

############################################################
################# NUMBER THEORY AND ALGEBRA ################
############################################################

# 26
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

# 48
def modular_exponentiate(n, exp, modulus):
    """Raise n to the exp with respect to modulus"""
    result = 1
    for i in range(exp):
        result = (n * result) % modulus
    return result

def polynomial_roots(coefficients):
    # Assumes coefficients = [a_0, a_1,..., a_n]
    # for f(x) = a_n x^n + ... + a_1 x + a_0
    if len(coefficients) != 3:
        raise ValueError("Only supporting quadratics at this time")
    c, b, a = coefficients
    discriminant_rt = sqrt(b**2 - 4*a*c)
    return [(-b + discriminant_rt)/(2.0*a), (-b - discriminant_rt)/(2.0*a)]

# 6, 42, 44, 61
def polygonal_number(s, n):
    return n*((s - 2)*n - (s - 4))/2

# 42, 44, 61
def reverse_polygonal_number(sides, number, hash_={}):
    """
    Returns n given that number is the nth polygonal
    number with respect to sides

    The n-th polygonal number for s sides is:
    n*((s - 2)*n - (s - 4))/2
    """
    if number in hash_:
        return hash_[number]
    root_plus, _ = polynomial_roots([-2*number, 4 - sides, sides - 2])
    if root_plus != int(root_plus):
        result = -1
    else:
        result = int(root_plus)
    if hash_ != {}:
        hash_[number] = result
    return result

# 72
def mu(n, hash_, primes):
    if n in hash_:
        return hash_[n]

    prime, _ = first_prime_divisor(n, prime_list=primes)
    if n % prime**2 == 0:
        hash_[n] = 0
    else:
        # if n/prime has a square, we will want mu(n) = 0
        # if mu(n/prime) = 1, we add 1 prime so we negate it
        # similarly if mu(n/prime) = -1
        hash_[n] = -mu(n/prime, hash_, primes)
    return hash_[n]

############################################################
###################### LIST MANAGEMENT #####################
############################################################

# 4, 23, 29, 56
def apply_to_list(func, list_, non_match=False):
    result = []
    for elt1 in list_:
        for elt2 in list_:
            if non_match:
                if elt1 != elt2:
                    result.append(func(elt1, elt2))
            else:
                result.append(func(elt1, elt2))
    return result

# 35, 41, 68, 121
def all_permutations(list_, duplicates=False):
    if len(list_) == 1:
        return [list_]

    result = []
    for element in list_:
        curr = list_[:]
        curr.remove(element)
        to_add = [[element] + sub_list
                  for sub_list in all_permutations(curr,
                                                   duplicates=duplicates)]
        if duplicates:
            result.extend([sub_list for sub_list in to_add
                           if sub_list not in result])
        else:
            result.extend(to_add)
    return result

# 35, 41
def all_permutations_digits(n):
    digs = [dig for dig in str(n)]
    result = all_permutations(digs, duplicates=True)
    return [int("".join(perm)) for perm in result]

# 49, 51, 60
def all_subsets(list_, size):
    if len(list_) < size:
        raise("List too small.")

    # Base case
    if size == 1:
        return [[element] for element in list_]

    # We can assume size > 1
    result = []
    for i in range(len(list_) - size + 1):
        curr = list_[i + 1:]
        result.extend([[list_[i]] + sub_list
                       for sub_list in all_subsets(curr, size - 1)])
    return result
