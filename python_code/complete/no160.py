from math import floor
from math import log

from python_code.functions import extended_euclid
from python_code.functions import inverse_mod_n
from python_code.functions import robust_divide

# f(9)=36288
# f(10)=36288
# f(20)=17664

def unit_a_zero_b(a, b):
    _, multiplier = extended_euclid(a, b)
    return (multiplier*b) % (a*b)

def num_factors_fact(n, factor):
    result = 0
    power = factor
    while n >= power:
        result += n/power
        power = factor*power
    return result

def f(n):
    if n < 8:
        # The remaining part is always divisible by
        # 2**5 for n > 7, these are special cases
        solutions = {0: 1,
                     1: 1,
                     2: 2,
                     3: 6,
                     4: 24,
                     5: 12,
                     6: 72,
                     7: 504}
        return solutions[n]

    if n <= 5**5:
        residues = {}
        for i in range(1, n + 1):
            to_add = robust_divide(i, 5)
            if to_add in residues:
                residues[robust_divide(i, 5)] += 1
            else:
                residues[robust_divide(i, 5)] = 1
    else:
        residues = {}
        for residue in range(1, 5**5):
            if residue % 5 != 0:
                residues[residue] = (n - residue)/(5**5) + 1
        max_power = int(floor(log(n)/log(5)))
        for power in range(1, max_power + 1):
            biggest_quotient = n/(5**power)
            for residue in range(1, 5**5):
                if residue % 5 != 0:
                    residues[residue] += (biggest_quotient - residue)/(5**5) + 1

    product = 1
    for residue, power in residues.items():
        power_apply = power % (4*(5**4)) # PHI(5**5)
        product = (product*(residue**power_apply)) % (5**5)
    fives = num_factors_fact(n, 5) % (4*(5**4)) # PHI(5**5)
    inverse = inverse_mod_n(2, 5**5)
    product = (product*(inverse**fives)) % (5**5)

    return (product*unit_a_zero_b(5**5, 2**5)) % 10**5

print f(10**12)
