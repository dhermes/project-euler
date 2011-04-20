from python_code.functions import get_data

data = [[int(dig) for dig in row] for row
        in get_data(79).split("\r\n") if row]

matches = {}
for attempt in data:
    a, b, c = attempt
    keys = [((a, b), (c, 'Right')),
            ((a, c), (b, 'Middle')),
            ((b, c), (a, 'Left'))]
    for key, val in keys:
        if key in matches:
            matches[key].append(val)
        else:
            matches[key] = [val]

for val in matches.values():
    val.sort()

# 73162890
# no (7, a) have left values so we choose 7 as the leftmost
# The majority of (b, a) with no left value are in 7 and 3
# so we start 73. Using the pairs with 7 and 3 first,
# and no left values we can put together the solution
# and verify it gels with all the conditions
print 73162890
