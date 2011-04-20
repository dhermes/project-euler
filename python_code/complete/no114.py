# the black are insignificant
# with k blocks, we simply can remove k - 1 blocks (dividers)
# and reconsider the problem

# We need k blocks to sum to less than or equal to 50 - (k-1)
# and can then fill the rest in with black blocks

# 0 <= sum(a_k - 3) <= 50 - 3k - (k - 1) = 51 - 4k

from math import factorial
import operator

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
    return factorial(sum(counts))/reduce(operator.mul, [factorial(count) for count in counts])

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

count = 1
MAX_k = 51/4
for k in range(1, MAX_k + 1):
    for sum_ai in range(3*k, 51 - k + 1):
        perm_count = 0
        for bottom in range(3, sum_ai/k + 1):
            for gp_ai in ascending(k, sum_ai, bottom, 50 + 1):
                perm_count += total_perms(gp_ai)
        count += perm_count*(factorial(51 - sum_ai)/(factorial(k)*factorial(51 - sum_ai - k)))
print count
