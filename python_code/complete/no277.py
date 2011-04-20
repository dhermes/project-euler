def sequence(letters, p_3, c, P_2):
    if letters == '':
        return p_3, c, P_2

    to_apply = letters[-1]
    if to_apply == 'D':
        return sequence(letters[:-1], p_3 + 1, 3*c, P_2)
    elif to_apply == 'U':
        return sequence(letters[:-1], p_3 + 1, 3*c - 2*P_2, 4*P_2)
    elif to_apply == 'd':
        return sequence(letters[:-1], p_3 + 1, 3*c + P_2, 2*P_2)

p_3, c, P_2 = sequence('UDDDUdddDDUDDddDdDddDDUDDdUUDd', 0, 0, 1)
print ((10**15)*P_2 - c)/(1.0*(3**p_3))
print "%sy == %s mod %s" % (3**p_3 % P_2, -c % P_2, P_2)
print "%sy == %s mod %s" % ((3**p_3 % P_2)/15, (-c % P_2)/15, P_2)
print "y == %s mod %s" % (((-c % P_2)/15 * 1886983) % P_2, P_2)
bottom = (((10**15)*P_2 - c)/(3**p_3))/P_2 + 1
y = P_2*bottom + ((-c % P_2)/15 * 1886983) % P_2
print ((3**p_3)*y + c) % P_2, ((3**p_3)*y + c)/P_2
print ((3**p_3)*y + c)/P_2 > 10**15
