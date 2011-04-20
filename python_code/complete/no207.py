from math import log

L = 1
while 12345*L + 1 >= 2**L:
    L += 1

count = 1
for n in range(2, 2**L):
    power = int(log(n + 1)/log(2))
    if n + 1 == 2**power:
        count += 1
    if 12345*count < n:
        break

print n*(n + 1)
