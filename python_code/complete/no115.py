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

def F(m, n):
    count = 1
    MAX_k = (n + 1)/(m + 1)
    for k in range(1, MAX_k + 1):
        for sum_ai in range(m*k, n + 1 - k + 1):
            perm_count = 0
            for bottom in range(m, sum_ai/k + 1):
                for gp_ai in ascending(k, sum_ai, bottom, n + 1):
                    perm_count += total_perms(gp_ai)
            count += perm_count*(factorial(n + 1 - sum_ai)/(factorial(k)*factorial(n + 1 - sum_ai - k)))
    return count

fill_count = 2
n = 50
while fill_count <= 10**6:
    n += 1
    fill_count = F(50, n)
print n
