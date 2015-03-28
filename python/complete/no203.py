#!/usr/bin/env python

# Find the sum of the distinct squarefree numbers in the first 51
# rows of Pascal's triangle.

from python.decorators import euler_timer
from python.functions import first_prime_divisor
from python.functions import robust_divide


def pascal_next(row):
    if len(row) < 2:
        raise ValueError("Don't pass this, breaks algorithm")

    result = [1]
    result.extend([row[i] + row[i + 1] for i in range(len(row) - 1)])
    # n = row[1], when n is odd the regular pascal row has
    # n + 1 = even number of elements, hence there is a repeat
    # in the middle
    if row[1] % 2 == 1:
        result.append(row[-1] * 2)
    return result


def unique_in_pascal(rows):
    if rows < 1:
        raise ValueError("Rows should be positive")
    elif rows < 3:
        return [1]

    vals = set([1, 2])
    curr = [1, 2]
    for i in range(4, rows + 1):
        curr = pascal_next(curr)
        vals.update(curr)
    return sorted(list(vals))


def is_squarefree(n):
    if n == 1:
        return True

    quotient = n
    count = 1
    while count == 1:
        prime, _ = first_prime_divisor(quotient)
        quotient, count = robust_divide(quotient, prime, include_count=True)
        if quotient == 1:
            return (count == 1)
    return False


def main(verbose=False):
    NUM_ROWS = 51
    pascal_vals = unique_in_pascal(NUM_ROWS)
    return sum(val for val in pascal_vals if is_squarefree(val))

if __name__ == '__main__':
    print euler_timer(203)(main)(verbose=True)
