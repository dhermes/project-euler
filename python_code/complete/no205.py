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

OUTCOMES_4 = {}
for bottom in range(1, 4 + 1):
    for dice_sum in range(1*9, 4*9 + 1):
        for outcome in ascending(9, dice_sum, bottom, 4):
            curr_sum = sum(outcome)
            if curr_sum in OUTCOMES_4:
                OUTCOMES_4[curr_sum] += total_perms(outcome)
            else:
                OUTCOMES_4[curr_sum] = total_perms(outcome)

OUTCOMES_6 = {}
for bottom in range(1, 6 + 1):
    for dice_sum in range(1*6, 6*6 + 1):
        for outcome in ascending(6, dice_sum, bottom, 6):
            curr_sum = sum(outcome)
            if curr_sum in OUTCOMES_6:
                OUTCOMES_6[curr_sum] += total_perms(outcome)
            else:
                OUTCOMES_6[curr_sum] = total_perms(outcome)

winning_outcomes = 0
for pete_score in range(9, 36 + 1):
    for colin_score in range(6, pete_score):
        winning_outcomes += OUTCOMES_4[pete_score]*OUTCOMES_6[colin_score]

print round(winning_outcomes*1.0/((4**9)*(6**6)), 7)
