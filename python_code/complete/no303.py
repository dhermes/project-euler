from itertools import product as i_product
from python_code.functions import prime_factors

def find(n, value_list):
    for value in value_list:
        if value % n == 0:
            return value

    digs = len(str(max(value_list)))
    needed_residues = sorted(set([(-value) % n for value in value_list]))

    residue = (10**digs) % n
    actual_list = [1, 2]
    residue_form = [(residue*val) % n for val in actual_list]
    while set(residue_form).intersection(needed_residues) == set():
        next = []
        for val in actual_list:
            next.extend([10*val, 10*val + 1, 10*val + 2])
        actual_list = next
        residue_form = [(residue*val) % n for val in actual_list]

    best_match = min([val for val in actual_list if (residue*val) % n in needed_residues])
    best_opposites = [val for val in value_list if val % n == (-(best_match*residue)) % n]
    return (10**digs)*best_match + min(best_opposites)

candidate_lists = [['0', '1', '2']]*12

values = list(i_product(*candidate_lists))
values = [int(''.join(value)) for value in values][1:]

running_sum = 0
for n in range(1, 10000 + 1):
    val = find(n, values)
    if val is None:
        print n
    else:
        running_sum += val/n
print running_sum
