from math import sqrt

from python_code.functions import sieve

def find_raw_solution(prime):
    max_n = int(sqrt(prime))
    for x in range(1, max_n + 1):
        y = int(sqrt(prime - x**2))
        if x**2 + y**2 == prime:
            return (x, y)
    return None

def complex_multiply(pair1, pair2):
    x1, y1 = pair1
    x2, y2 = pair2
    new_x = x1*x2 - y1*y2
    new_y = x1*y2 + x2*y1
    if abs(new_y) > abs(new_x):
        new_x, new_y = new_y, -new_x
    if new_x < 0:
        new_x = -new_x
        new_y = -new_y

    return (new_x, new_y)

PRIMES = [prime for prime in sieve(150) if prime % 4 == 1]

product_hash = {1: set([(1, 0)])}
for prime in PRIMES:
    x, y = find_raw_solution(prime)
    for key, value in product_hash.items():
        to_add = set()
        for pair in value:
            to_add.update([complex_multiply((x, y), pair),
                           complex_multiply((x, -y), pair)])
        product_hash[prime*key] = to_add

running_sum = 0
for key, value in product_hash.items():
    if key == 1:
        continue
    for big, small in value:
        if small > 0:
            running_sum += small
print running_sum
