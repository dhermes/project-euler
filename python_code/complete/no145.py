# leading and trailing zeroes are bad
def reverse(n):
    return int(str(n)[::-1])

def all_odd(val):
    return 0 not in [int(dig) % 2 for dig in str(val)]

n = 10**3
count = 0
hash_ = {}
for i in range(1, n + 1):
    if i % 10 != 0:
        if i in hash_:
            if hash_[i]:
                count += 1
        else:
            rev = reverse(i)
            if all_odd(i + rev):
                count += 1
                hash_[i] = True
                hash_[rev] = True
            else:
                hash_[i] = False
                hash_[rev] = False
print count

matches = [key for key, value in hash_.items() if value]
match_h = {}
for val in matches:
    length = len(str(val))
    if length in match_h:
        match_h[length].append(val)
    else:
        match_h[length] = [val]

a2 = [(x, reverse(x)) for x in match_h[2] if x <= reverse(x) ]
a3 = [(x, reverse(x)) for x in match_h[3] if x <= reverse(x) ]
# a4 = [(x, reverse(x)) for x in match_h[4] if x <= reverse(x) ]
# a6 = [(x, reverse(x)) for x in match_h[6] if x <= reverse(x) ]
# a7 = [(x, reverse(x)) for x in match_h[7] if x <= reverse(x) ]
