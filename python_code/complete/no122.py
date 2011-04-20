def next_possible(chain):
    candidates = []
    for i in range(len(chain)):
        for j in range(i, len(chain)):
            candidates.append(chain[i] + chain[j])
    return [cand for cand in sorted(candidates) if cand > max(chain)]

def find_min_brauers(n):
    result = {1: [1], 2: [1, 2]}

    chains = [[1,2]]
    # while len(result) < n:
    while max(result) < n:
        new_chains = []
        for chain in chains:
            candidates = next_possible(chain)
            for candidate in candidates:
                if candidate not in result and candidate <= n:
                    result[candidate] = chain + [candidate]
            new_chains.extend([chain + [cand] for cand in candidates])
        chains = new_chains

    return result

MAX_n = 200
brauers = find_min_brauers(MAX_n)

missing = [i for i in range(1, MAX_n + 1) if i not in brauers]
m_vals = {127: [1, 2, 3, 4, 7, 8, 15, 30, 60, 67, 127],
          139: [1, 2, 3, 4, 7, 10, 17, 34, 68, 71, 139],
          141: [1, 2, 3, 4, 7, 10, 20, 27, 47, 94, 141],
          142: [1, 2, 3, 4, 7, 8, 16, 32, 39, 71, 142],
          143: [1, 2, 3, 4, 7, 10, 17, 34, 68, 75, 143],
          151: [1, 2, 3, 4, 7, 9, 18, 36, 72, 79, 151],
          155: [1, 2, 3, 4, 7, 11, 18, 36, 72, 83, 155],
          157: [1, 2, 3, 5, 7, 12, 19, 38, 76, 81, 157],
          158: [1, 2, 3, 4, 7, 9, 18, 36, 43, 79, 158],
          159: [1, 2, 3, 4, 8, 16, 19, 35, 70, 89, 159],
          167: [1, 2, 3, 4, 7, 10, 20, 40, 80, 87, 167],
          169: [1, 2, 3, 4, 7, 14, 21, 42, 84, 85, 169],
          171: [1, 2, 3, 4, 7, 14, 21, 42, 84, 87, 171],
          173: [1, 2, 3, 5, 7, 14, 21, 42, 84, 89, 173],
          174: [1, 2, 3, 4, 7, 10, 20, 40, 47, 87, 174],
          175: [1, 2, 3, 4, 7, 14, 21, 35, 70, 105, 175],
          177: [1, 2, 3, 4, 7, 11, 22, 44, 88, 89, 177],
          178: [1, 2, 3, 4, 7, 11, 22, 44, 45, 89, 178],
          179: [1, 2, 3, 4, 7, 11, 22, 44, 88, 91, 179],
          181: [1, 2, 3, 5, 6, 11, 22, 44, 88, 93, 181],
          182: [1, 2, 3, 4, 7, 11, 22, 44, 47, 91, 182],
          183: [1, 2, 3, 4, 7, 11, 22, 44, 88, 95, 183],
          185: [1, 2, 3, 5, 8, 16, 21, 37, 74, 111, 185],
          186: [1, 2, 3, 4, 7, 14, 17, 31, 62, 93, 186],
          187: [1, 2, 3, 4, 7, 11, 22, 44, 88, 99, 187],
          188: [1, 2, 3, 4, 7, 10, 20, 27, 47, 94, 188],
          189: [1, 2, 3, 4, 7, 14, 21, 42, 63, 126, 189],
          190: [1, 2, 3, 4, 7, 11, 22, 44, 51, 95, 190],
          191: [1, 2, 3, 4, 7, 8, 15, 22, 44, 88, 103, 191],
          197: [1, 2, 3, 5, 6, 12, 24, 48, 96, 101, 197],
          199: [1, 2, 3, 5, 7, 12, 24, 48, 96, 103, 199]}
if sorted(missing) != sorted(m_vals.keys()):
    raise Exception("BAD")

for value in m_vals:
    brauers[value] = m_vals[value][:]

print sum([len(value) - 1 for value in brauers.values()])
