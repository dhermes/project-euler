#!/usr/bin/env python

# A particular school offers cash rewards to children with good attendance
# and punctuality. If they are absent for three consecutive days or late
# on more than one occasion then they forfeit their prize.

# During an n-day period a trinary string is formed for each child
# consisting of L's (late), O's (on time), and A's (absent).

# Although there are eighty-one trinary strings for a 4-day period
# that can be formed, exactly forty-three strings would lead to a prize:

# How many "prize" strings exist over a 30-day period?

#######################################
# Let T{n} be the total number of such days
# We split this into several sequences
# O_N{n} - most recent day is on time, no L encountered
# O_L{n} - most recent day is on time, L encountered
# L_L{n} - most recent day is late, L encountered
# A_N{n} - most recent day is absent, day prior was not, no L encountered
# A_L{n} - most recent day is absent, day prior was not, L encountered
# T_N{n} - most recent two days are absent, day prior was not, no L encountered
# T_L{n} - most recent two days are absent, day prior was not, L encountered

from python.decorators import euler_timer


def prize_strings(n):
    index = 1
    O_N = 1
    O_L = 0
    L_L = 1
    A_N = 1
    A_L = 0
    T_N = 0
    T_L = 0
    while index < n:
        # after O, next can be anything:
        #     O_L-->O_L,A_L; O_N-->O_N,A_N,L_L
        # after one A, next can be anything
        #     A_L-->T_L,O_L; A_N-->O_N,T_N,L_L
        # after two A's, next can not be A
        #     T_L-->O_L; T_N-->O_N,L_L
        # after L is encountered, no more L
        # L_L-->O_L,A_L
        index += 1
        O_N, O_L, L_L, A_N, A_L, T_N, T_L = (O_N + A_N + T_N,
                                             O_L + A_L + T_L + L_L,
                                             O_N + A_N + T_N,
                                             O_N,
                                             O_L + L_L,
                                             A_N,
                                             A_L)
    return O_N + O_L + L_L + A_N + A_L + T_N + T_L


def main(verbose=False):
    return prize_strings(30)

if __name__ == '__main__':
    print euler_timer(191)(main)(verbose=True)
