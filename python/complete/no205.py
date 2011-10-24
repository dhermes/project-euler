#!/usr/bin/env python

from python.decorators import euler_timer
from python.functions import ascending
from python.functions import total_perms

def dice_outcomes(num_dice, num_sides):
    result = {}
    for bottom in range(1, num_sides + 1):
        for dice_sum in range(1*num_dice, num_sides*num_dice + 1):
            for outcome in ascending(num_dice, dice_sum, bottom, num_sides):
                curr_sum = sum(outcome)
                # if curr_sum is not in result, sets to total_perms(outcome)
                # (default 0 returned by get)
                result[curr_sum] = result.get(curr_sum, 0) + \
                                   total_perms(outcome)
    return result

def main(verbose=False):
    OUTCOMES_4 = dice_outcomes(9, 4)
    OUTCOMES_6 = dice_outcomes(6, 6)

    winning_outcomes = 0
    for pete_score in range(9, 36 + 1):
        for colin_score in range(6, pete_score):
            winning_outcomes += OUTCOMES_4[pete_score]*OUTCOMES_6[colin_score]

    return round(winning_outcomes*1.0/((4**9)*(6**6)), 7)

if __name__ == '__main__':
    print euler_timer(205)(main)(verbose=True)
