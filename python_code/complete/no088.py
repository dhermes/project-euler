from python_code.functions import all_factors

MAX_n = 13000
factor_hash = {1: [1]}
factor_hash = all_factors(MAX_n, factor_hash)
available = {}
for i in range(1, MAX_n + 1):
    available[i] = [factor for factor in factor_hash[i]
                    if factor > 1 and factor**2 <= i]

new_hash = {1: [[]], 2: [[2]]}
value_hash = {}
for i in range(3, 13000 + 1):
    to_add = [[i]]
    for factor in available[i]:
        for subset1 in new_hash[factor]:
            for subset2 in new_hash[i/factor]:
                cand = sorted(subset1 + subset2)
                if cand not in to_add:
                    to_add.append(cand)
    for match in to_add:
        new_k = i + len(match) - sum(match)
        if new_k > 1 and new_k not in value_hash:
            value_hash[new_k] = i
    new_hash[i] = to_add

final_list = []
for desired in range(2, 12001):
    if desired not in value_hash:
        raise Exception("Subset not large enough, raise MAX_n.")
    if value_hash[desired] not in final_list:
        final_list.append(value_hash[desired])

print sum(final_list)
