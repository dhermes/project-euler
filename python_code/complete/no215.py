def special_perms(num_2, num_3):
    if num_3 == 0:
        return [[2]*num_2]
    elif num_2 == 0:
        return [[3]*num_3]

    result = [[2] + perm for perm in special_perms(num_2 - 1, num_3)] + \
             [[3] + perm for perm in special_perms(num_2, num_3 - 1)]
    return result

def cumulative_sum(list_):
    result = [list_[0]]
    for entry in list_[1:]:
        result.append(result[-1] + entry)
    return result

def valid_arrange(depth, acceptable):
    if depth < 1:
        raise Exception("DUMB INPUT")
    elif depth == 1:
        return [[key] for key in acceptable]

    result = []
    for arrange in valid_arrange(depth - 1, acceptable):
        last = arrange[-1]
        result.extend([arrange + [next] for next in acceptable[last]])
    return result

# 2x + 3y = 32
# implies y = 2y*, x = 16 - 3y* for 0 <= y* <= 5

break_rows = []
for y_star in range(5 + 1):
    x = 16 - 3*y_star
    y = 2*y_star
    for perm in special_perms(x, y):
        to_add = cumulative_sum(perm)
        if to_add[-1] != 32:
            raise ValueError("FIX IT")
        break_rows.append(to_add[:-1])

acceptable_next = {}
for i, row in enumerate(break_rows):
    to_add = []
    for j, onto_row in enumerate(break_rows):
        if set(row).intersection(onto_row) == set():
            to_add.append(j)
    acceptable_next[i] = to_add

num_blocks_ending = {}
for key in acceptable_next:
    num_blocks_ending[key] = {1: 1}

blocks = 1
while blocks < 10:
    blocks += 1
    for key, value in acceptable_next.items():
        for onto in value:
            if blocks in num_blocks_ending[onto]:
                num_blocks_ending[onto][blocks] += num_blocks_ending[key][blocks - 1]
            else:
                num_blocks_ending[onto][blocks] = num_blocks_ending[key][blocks - 1]

result = 0
for key in num_blocks_ending:
    result += num_blocks_ending[key][10]
print result
