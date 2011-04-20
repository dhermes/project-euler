D=[[[1]]]
s=0
for k in range(2, 201):
    A=[]
    for t in D:
        for v in t:
            for a in v:
                b = k - a
                if b >= a and b in v:
                    to_add = v[:] + [k]
                    if to_add not in A:
                        A.append(to_add)
    m = min(len(a) for a in A)
    D.append([])
    for a in A:
        if len(a) == m:
            D[-1].append(a)
    s += m-1

print s
