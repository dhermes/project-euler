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

def generate_addons(num, smallest, biggest):
    if num == 1:
        return [[i] for i in range(smallest, biggest + 1)]

    result = []
    for i in range(smallest, biggest + 1):
        result.extend([[i] + addon for addon in generate_addons(num-1, i, biggest)])
    return result

MATCHES = []
for bottom in range(1, 12 + 1):
    MATCHES.extend(ascending(10, 70, bottom, 12))

add_ons = {}
for biggest in range(1, 8):
    add_ons[biggest] = generate_addons(10, 1, biggest)

count = 0
for match in MATCHES:
    bottom = match[0]
    for addon in add_ons[bottom]:
        curr = addon + match
        count += total_perms(curr)
print count
