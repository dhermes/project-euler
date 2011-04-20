from math import floor
from math import log

# 2(1 + 2 + ... + 2**(k - 2)) = 2**k - 2 < 2**k
# So 2**k <= n < 2**(k + 1)
# means we must end in one of
# 2**(k - 1), 2*(2**(k - 1)), 2**k, 2**(k - 1) + 2**k

def f_helper2(n, max_power):
    if n == 0:
        return 1
    if max_power == 0:
        if n in [1, 2]:
            return 1
        else:
            return 0

    result = f_helper2(n, max_power - 1)
    if n >= 2**max_power:
        result += f_helper2(n - 2**max_power, max_power - 1)
    if n >= 2**(max_power + 1):
        result += f_helper2(n - 2**(max_power + 1), max_power - 1)
    return result

def f2(n):
    max_power = int(floor(log(n)/log(2)))
    return f_helper2(n, max_power)

def f(n, hash_={}):
    if n in hash_:
        return hash_[n]
    if n in [1, 2]:
        hash_[n] = n
        return n
    if n % 2 == 0:
        result = f(n/2) + f(n/2 - 1)
    else:
        result = f((n - 1)/2)
    hash_[n] = result
    return result

f_hash = {}
print f(10**25, f_hash)

# 10 3
# 10 2
# 10 1
# 10 0
# 8 0
# 6 0
# 6 1
# 6 0
# 4 0
# 2 0
# 2 1
# 2 0
# 0 0
# 2 2
# 2 1
# 2 0
# 0 0
