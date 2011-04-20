from math import sqrt

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

def short_distance_int(a, b, c):
    best = min(sqrt(a**2 + (b + c)**2),
               sqrt(b**2 + (c + a)**2),
               sqrt(c**2 + (a + b)**2))
    return int(best) == best

def num_solutions(M, hash_):
    if M in hash_:
        return hash_[M]
    if M == 0:
        hash_[0] = 0
        return 0

    to_add = 0
    for lowest in range(1, M):
        # exactly 1 values M
        for mid in range(lowest, M):
            if short_distance_int(lowest, mid, M):
                to_add += 1
        # exactly 2 values M
        if short_distance_int(lowest, M, M):
            to_add += 1
    # all values M
    if short_distance_int(M, M, M):
        to_add += 1
    result = to_add + num_solutions(M - 1, hash_)
    hash_[M] = result
    return result

TARGET = 10**6
solution_hash = {0: 0}
M = 1
num_solutions(1, solution_hash)
while solution_hash[M] <= TARGET:
    M += 1
    num_solutions(M, solution_hash)
print M, solution_hash[M]
# 1818
