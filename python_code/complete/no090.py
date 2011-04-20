from python_code.functions import all_subsets
# def all_subsets(list_, size):

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

def can_concat(left, right):
    possible = ['%s%s' % (dig_l, dig_r) for dig_l in left for dig_r in right]
    possible.extend(['%s%s' % (dig_l, dig_r) for dig_l in right for dig_r in left])
    return (len(set(possible).intersection(
        ['01', '04', '09', '16', '25', '36', '49', '64', '81'])) == 9)

dice = all_subsets(range(10), 6)
size = len(dice)
for i in range(size):
    if 6 in dice[i]:
        if 9 not in dice[i]:
            dice[i].append(9)
    if 9 in dice[i]:
        if 6 not in dice[i]:
            dice[i].append(6)

count = 0
for left_ind in range(size - 1):
    for right_ind in range(left_ind, size):
        if can_concat(dice[left_ind], dice[right_ind]):
            count += 1
print count
