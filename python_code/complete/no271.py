from itertools import product as i_product
from python_code.functions import prime_factors

def extended_euclid(a, b):
    M = max(a, b)
    m = min(a, b)

    last = (M, [1, 0])
    curr = (m, [0, 1])
    while curr[0] > 1:
        next = last[0] % curr[0]
        factor = (last[0] - next)/curr[0]
        last, curr = curr, (next, [last[1][0] - factor*curr[1][0], last[1][1] - factor*curr[1][1]])
    result = curr[1]
    if a*result[0] + b*result[1] == 1:
        return result
    else:
        return result[::-1]

def find_cube_roots(prime):
    # Won't check, but assumes prime is prime
    # in a prime field x^3 == 1 implies x == 1 or x^2 + x + 1 == 0
    # since a domain, the latter is satisfied if
    # (2x + 1)**2 == -3 mod prime (so we handle 2 and 3 differently)
    if prime in [2, 3]:
        return [1]

    # The inverse of 2 is (prime + 1)/2
    # If L(q,p) is the legendre symbol, for p != 2 or 3 we know
    # L(-3, p) = L(-1, p)*L(3, p) = (-1)**(floor((p+1)/6)+(p-1)/2)
    if (-1)**((prime + 1)/6 + (prime - 1)/2) == -1:
        return [1]

    for i in xrange(1, prime):
        if (i**2 + 3) % prime == 0:
            break
    # So we know i and prime - i are the square roots of 3
    return sorted([1, ((prime + 1)*(i - 1)/2) % prime, ((prime + 1)*(prime - i - 1))/2 % prime])

product = 13082761331670030
factors = prime_factors(product)

candidate_lists = []
for factor in factors:
    candidate_lists.append([(factor, root) for root in find_cube_roots(factor)])

# result = [[]]
# for prime, solns in d.items():
#     curr = []
#     for ans in result:
#         for soln in solns:
#             curr.append([(prime, soln)] + ans)
#     result = curr
result = list(i_product(*candidate_lists))

# P = product(factors)
# s (P/f_i) + r f_i = 1
# Set e_i = s (P/f_i)
# Then e_i + 0 == 1 mod f_i
# and by definition e_i = s(0) mod f_j
# Then the solution will be (sum res_i*e_i) mod P

coprime_units = {}
for factor in factors:
    _, multiplier = extended_euclid(factor, product/factor)
    coprime_units[factor] = multiplier*(product/factor)

vals = []
for pairing in result:
    count = 0
    for prime, residue in pairing:
        count += residue*coprime_units[prime]
    count = count % product
    vals.append(count)

print sum(vals) - 1 # 1 is in there as (1,1,...,1)
