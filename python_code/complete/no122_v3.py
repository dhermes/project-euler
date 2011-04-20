lim = 200

best = [None, [set([1])]]
for exp in range(2, lim + 1):
    facts = []
    for f1 in xrange(1, exp / 2 + 1):
        for constr in best[exp - f1]:
            if f1 in constr: facts.append(constr.union([exp]))
    bestlen = min(len(fact) for fact in facts)
    best.append([fact for fact in facts if len(fact) == bestlen])

print sum(len(b[0]) - 1 for b in best[1:])
