def inc_or_dec(n):
    digs = [dig for dig in str(n)]
    if sorted(digs) == digs:
        return True
    elif sorted(digs) == digs[::-1]:
        return True
    else:
        return False

n = 21780
B = 19602 # 90%
while 100*B != 99*n:
    n += 1
    if not inc_or_dec(n):
        B += 1
print n
