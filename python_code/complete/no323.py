from math import factorial

def choose(n, k):
    return factorial(n)/(factorial(k)*factorial(n - k))

# The problem is a generalization of one when n = 32
# Let E(N)_n = the expected value when the y_i, x_i
# have n bits. Then
# 2**n E(N)_n = sum_{k=0 to n} (n choose k) [E(N)_{n - k} + 1]
# 2**n E(N)_n = 2**n + sum_{k=0 to n} (n choose k) E(N)_{n - k}
# (2**n - 1) E(N)_n = 2**n + sum_{k=1 to n} (n choose k) E(N)_{n - k}

# This is because of the 2**n outcomes for y_1, (n choose k)
# have k bits set to 1. In those situations, the expected time
# will be 1 + E(N)_{n - k} since the non-zero bits are static going
# forward, the problem reduces to the digits unset

expected_hash = {0: 0}
for n in range(1, 32 + 1):
    to_add = 2**n
    for k in range(1, n + 1):
        to_add += choose(n, k)*expected_hash[n - k]
    expected_hash[n] = (to_add*1.0)/(2**n - 1)

print round(expected_hash[32], 10)
