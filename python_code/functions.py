from os import path as opath
import sys

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

# 21, 27, 37
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

# 25
def fibonacci_generator():
    """a generator for Fibonacci numbers"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
