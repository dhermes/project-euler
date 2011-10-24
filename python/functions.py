import operator
import sys

from fractions import gcd
from math import factorial
from math import log
from math import sqrt

from path import DATA_PATH

############################################################
##################### HELPER FUNCTIONS #####################
############################################################

def lcm(n, m):
    return n*m/(gcd(n, m))

def choose(n, k):
    return factorial(n)/(factorial(k)*factorial(n - k))

# 8, 11, 13, 18, 22, 42, 54, 59, 67
def get_data(problem_number):
    """
    Takes a problem number and returns the raw text
    from the expected data file

    Data is expected to be in euler_project/problem_data and
    to be named no---.txt where --- is the zero padded
    problem number
    """
    filename = 'no%s.txt' % str(problem_number).zfill(3)
    absolute_path = '%s/%s' % (DATA_PATH, filename)
    with open(absolute_path) as fh:
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
    next_val = sum(relation[i]*values[i] for i in range(recurrence_order))
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

# 114, 115
def fill_count(m, n):
    count = 1
    MAX_k = (n + 1)/(m + 1)
    for k in range(1, MAX_k + 1):
        for sum_ai in range(m*k, n + 1 - k + 1):
            perm_count = 0
            for bottom in range(m, sum_ai/k + 1):
                for gp_ai in ascending(k, sum_ai, bottom, n + 1):
                    perm_count += total_perms(gp_ai)
            add_value = perm_count*choose(n + 1 - sum_ai, k)
            count += add_value
    return count

# 132, 133
def prime_divides_repunit_power10(prime, cap=-1):
    # Determines if a prime divides any repunit R(10**n)
    # if cap > 0, then we set a max on the value of n
    if prime in [2, 3, 5]:
        return False
    _, count_2 = robust_divide(prime - 1, 2, include_count=True)
    _, count_5 = robust_divide(prime - 1, 5, include_count=True)
    if cap > 0:
        count_2 = min(cap, count_2)
        count_5 = min(cap, count_5)
    if prime == (2**count_2)*(5**count_5) + 1:
        return True
    possible_exp = sorted((2**exp2)*(5**exp5)
                          for exp2 in range(0, count_2 + 1)
                          for exp5 in range(0, count_5 + 1))
    for exp in possible_exp:
        if (10**exp - 1) % prime == 0:
            return True
    return False

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

def first_prime_divisor(n, prime_list=None):
    if n == 1:
        return [1, 1]
    elif n % 2 == 0:
        return [2, n/2]

    if prime_list is not None:
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
        divisor = 3
        while n % divisor != 0:
            divisor += 2
        return [divisor, n/divisor]
    raise ValueError("Bad input %s." % n)

# 3, 12, 47
def prime_factors(n, unique=False, hash_=None):
    if n == 1:
        if isinstance(hash_, dict):
            hash_[1] = []
        return []
    if isinstance(hash_, dict) and n in hash_:
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

    if isinstance(hash_, dict):
        hash_[n] = result

    return result

# 135
def factors(n, factor_hash=None, primes=None):
    if factor_hash is None:
        factor_hash = {}

    if n in factor_hash:
        return factor_hash[n]
    elif n == 1:
        factor_hash[1] = [1]
        return [1]

    if primes is not None and n in primes:
        factor_hash[n] = [1, n]
        return [1,n]

    prime, quotient = first_prime_divisor(n, prime_list=primes)

    to_add = factors(quotient, factor_hash, primes)[:] # Need a deep-ish copy
    to_add.extend([prime*factor for factor in to_add])

    factor_hash[n] = sorted(list(set(to_add)))
    return factor_hash[n]

# 21, 23, 39
def all_factors(n, hash_={1: [1], 2: [1, 2], 3: [1, 3]}):
    """
    Takes n and optional hash of factors

    Uses the hash to update a full list of factors for
    all integers 1 to n. Only updates if not in hash_.
    """
    factor_hash = hash_.copy()
    if n in factor_hash:
        return factor_hash

    all_primes = sieve(n)

    for i in range(4, n + 1):
        if i not in factor_hash:
            reduced = first_prime_divisor(i, all_primes)
            # This will update factor hash
            factors(i, factor_hash=factor_hash, primes=all_primes)

    return factor_hash

# 37, 41, 58
def is_prime(n, primes=None, failure_point=None):
    if n < 10:
        return n in [2, 3, 5, 7]

    # We safely assume n >= 10
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return False

    if failure_point is not None:
        if n >= failure_point:
            raise ValueError("%s is too large for is_prime." % n)

    if primes is not None:
        if n in primes:
            return True
        to_check = [prime for prime in primes if prime**2 <= n]
        for prime in to_check:
            if n % prime == 0:
                return False
        return True

    divisor_bound = int(sqrt(n))
    # From here, we know only +/- 1 mod 6 works, so
    # we start with 11 and 13 (primes > 10)
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
def order_mod_n(value, n, hash_=None, prime_list=None):
    if hash_ is None:
        hash_ = {}
    if n in hash_:
        return hash_[n]

    if gcd(value, n) != 1 or n == 1:
        raise ValueError("%s is not a unit modulo %s." % (value, n))

    prime, _ = first_prime_divisor(n, prime_list)
    quotient = robust_divide(n, prime)
    if quotient == 1:
        # at this point, n is not in the hash_ but must be a
        # prime power
        base_residue = value % n

        residue = base_residue
        exponent = 1
        while residue != 1:
            residue = (residue * base_residue) % n
            exponent += 1
        hash_[n] = exponent
        return exponent

    # Here, quotient > 1
    prime_power = n/quotient
    prime_order = order_mod_n(value, prime_power,
                              hash_=hash_,
                              prime_list=prime_list)
    quotient_order = order_mod_n(value, quotient,
                                 hash_=hash_,
                                 prime_list=prime_list)
    hash_[n] = lcm(prime_order, quotient_order)
    return hash_[n]

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
def reverse_polygonal_number(sides, number, hash_=None):
    """
    Returns n given that number is the nth polygonal
    number with respect to sides

    The n-th polygonal number for s sides is:
    n*((s - 2)*n - (s - 4))/2
    """
    if hash_ is not None and number in hash_:
        return hash_[number]
    root_plus, _ = polynomial_roots([-2*number, 4 - sides, sides - 2])
    if root_plus != int(root_plus):
        result = -1
    else:
        result = int(root_plus)

    if hash_ is not None:
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

def extended_euclid(a, b):
    M = max(a, b)
    m = min(a, b)

    last = (M, [1, 0])
    curr = (m, [0, 1])
    while curr[0] > 1:
        next = last[0] % curr[0]
        factor = (last[0] - next)/curr[0]
        last, curr = curr, (next, [last[1][0] - factor*curr[1][0],
                                   last[1][1] - factor*curr[1][1]])
    result = curr[1]
    if a*result[0] + b*result[1] == 1:
        return result
    else:
        return result[::-1]

def inverse_mod_n(val, n):
    if gcd(val, n) > 1:
        raise Exception("Not invertible")

    result, _ = extended_euclid(val, n)
    return result % n

# Let r_i = 1/(a_(i+1) + 1/(a(i+2) + ...
# Then 1/r_i = a_(i+1) + r_(i+1); a_i = floor(1/r_i)

# We see we can write r_i = (A_i*rt(n) + B_i)/C_i
# then 1/r_i = C_i(A_i*rt(n) - B_i)/(n*A_i**2 - B_i**2)

# represent each r_i as r_i = (A, B, C) -> 1/r_i = a + r_(i + 1)
# -> a = floor(1/r_i) = floor( C/(A rt(n) + B) )
# -> r_(i + 1) = (C*A, C*B - a*(n*A**2 - B**2), n*A**2 - B**2)
# -> r_(i + 1) = (A', B', C') #reduce
# then r_(i+1) = (C_i*A_i*rt(n) - [C_i*B_i + a_(i+1)*(n*A_i**2 - B_i**2)])/(n*A_i**2 - B_i**2)

def next_continued_fraction_triple(current, n):
    A, B, C = current
    a = int(C*(1.0)/(A*sqrt(n) + B))
    r = (C*A, -C*B - a*(n*A**2 - B**2), n*A**2 - B**2)
    d = gcd(gcd(r[0], r[1]), r[2])
    return (r[0]/d, r[1]/d, r[2]/d)

def continued_fraction_cycle(n):
    result = [int(sqrt(n))]
    init = curr_r = (1, -int(sqrt(n)), 1)

    result.append(int(curr_r[2]*(1.0)/(curr_r[0]*sqrt(n) + curr_r[1])))
    curr_r = next_continued_fraction_triple(curr_r, n)
    while curr_r != init:
        result.append(int(curr_r[2]*(1.0)/(curr_r[0]*sqrt(n) + curr_r[1])))
        curr_r = next_continued_fraction_triple(curr_r, n)
    return result

def power_up_to_digits(n, digits):
    return [n**exp for exp in range(int(digits*log(10)/log(n)) + 1)]

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
def all_permutations(list_):
    result = [[]]
    for i in range(len(list_)):
        extended = []
        for perm in result:
            for position in range(i + 1):
                extended.append(perm[:position] + [list_[i]] + perm[position:])
        result = extended
    return result

# 35, 41
def all_permutations_digits(n):
    digs = [dig for dig in str(n)]
    result = all_permutations(digs)
    return [int("".join(perm)) for perm in result]

# 49, 51, 60
def all_subsets(list_, size, unique=True):
    if len(list_) < size:
        if unique:
            raise ValueError("List too small.")

    # Base case
    if size == 1:
        if unique:
            return [[element] for element in set(list_)]
        else:
            return [[element] for element in list_]

    if not unique:
        return reduce(operator.add, [[[element] + subset for subset in
                                      all_subsets(list_, size - 1, False)]
                                     for element in list_])

    # We can assume size > 1
    result = []
    for i in range(len(list_) - size + 1):
        curr = list_[i + 1:]
        result.extend([[list_[i]] + sub_list
                       for sub_list in all_subsets(curr, size - 1)])
    return result

############################################################
######################## GRAPH THEORY ######################
############################################################

def astar(graph, start, target, heuristic, adjacent):
    closed_nodes = {start: (None, graph[start])}
    # node, parent, distance, don't store heuristic dist.

    open_nodes = {}
    for node in adjacent(start):
        if node in graph:
            open_nodes[node] = (start, graph[start] + graph[node])

    while target not in closed_nodes:
        min_val = None
        min_f = -1
        for node in open_nodes:
            val = open_nodes[node][1] + heuristic(node)
            if min_val is None:
                min_val = val
                min_f = node
            else:
                if val < min_val:
                    min_val = val
                    min_f = node

        closed_nodes[min_f] = open_nodes.pop(min_f)

        min_val = min_val - heuristic(min_f)
        for node in adjacent(min_f):
            if node not in graph or node in closed_nodes:
                continue
            if node in open_nodes:
                comp_val = open_nodes[node][1]
                new_val = min_val + graph[node]
                if new_val < comp_val:
                    open_nodes[node] = (min_f, new_val)
            else:
                open_nodes[node] = (min_f, min_val + graph[node])

    return closed_nodes[target][1]

def prims_algo(adjacency_list):
    keys = adjacency_list.keys()
    vertices = [keys[0]]
    keys = set(keys)
    edges = []
    min_sum = 0
    while set(vertices) != keys:
        # Find next edge
        candidates = {}
        for vertex in vertices:
            for node, val in adjacency_list[vertex]:
                if node not in vertices:
                    candidates[(vertex, node)] = val

        new_edge, val = sorted(candidates.items(), key=lambda pair: pair[1])[0]
        min_sum += val
        edges.append(new_edge)
        vertices.append(new_edge[1])

    return edges, min_sum

def total_perms(o_list):
    counts = []
    curr_entry = o_list[0]
    curr_count = 1
    for entry in o_list[1:]:
        if entry == curr_entry:
            curr_count += 1
        else:
            counts.append(curr_count)
            curr_entry = entry
            curr_count = 1
    counts.append(curr_count)

    denominator = reduce(operator.mul,
                         [factorial(count) for count in counts])
    return factorial(sum(counts))/denominator

def ascending(num, num_sum, min_num, prob_max):
    if num_sum < min_num:
        return []
    if num == 1:
        if num_sum == min_num:
            return [[num_sum]]
        else:
            return []

    next_sum = num_sum - min_num
    biggest = next_sum/(num - 1) # integer division intended
    biggest = min(biggest, prob_max)
    result = []
    for next_min in range(min_num, biggest + 1):
        result.extend([[min_num] + cand for cand in
                        ascending(num - 1, next_sum, next_min, prob_max)])
    return result
