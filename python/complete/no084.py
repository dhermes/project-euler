#!/usr/bin/env python

from random import choice

from python.decorators import euler_timer

SQUARES = ["GO",
           "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3",
           "JAIL",
           "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3",
           "FP",
           "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3",
           "G2J",
           "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"]


def roll_die(size):
    first_die = choice(range(1, size + 1))
    second_die = choice(range(1, size + 1))

    return (first_die + second_die, (first_die == second_die))


def back(square, step):
    index = SQUARES.index(square)
    new_index = (index - step) % len(SQUARES)
    return SQUARES[new_index]


def next_specific(square, next_type):
    if next_type not in ["R", "U"]:
        raise Exception("next_specific only intended for R and U")

    # R1=5, R2=15, R3=25, R4=35
    index = SQUARES.index(square)
    if next_type == "R":
        if 0 <= index < 5 or 35 < index:
            return "R1"
        elif 5 < index < 15:
            return "R2"
        elif 15 < index < 25:
            return "R3"
        elif 25 < index < 35:
            return "R4"
        else:
            raise Exception("Case should not occur")
    # U1=12, U2=28
    elif next_type == "U":
        if 0 <= index < 12 or index > 28:
            return "U1"
        elif 12 < index < 28:
            return "U2"
        else:
            return Exception("Case should not occur")
    else:
        raise Exception("Case should not occur")


def next_square(landing_square, chance_card, chest_card):
    if landing_square not in ["CC1", "CC2", "CC3", "CH1", "CH2", "CH3", "G2J"]:
        return (landing_square, chance_card, chest_card)

    if landing_square == "G2J":
        return ("JAIL", chance_card, chest_card)
    elif landing_square in ["CC1", "CC2", "CC3"]:
        # 1/16 Go, Jail
        # 14/16 Stay
        chest_card = (chest_card + 1) % 16
        if chest_card == 0:
            return ("GO", chance_card, chest_card)
        elif chest_card == 1:
            return ("JAIL", chance_card, chest_card)
        else:
            return (landing_square, chance_card, chest_card)
    elif landing_square in ["CH1", "CH2", "CH3"]:
        # 1/16 Go, Jail, C1, E3, H2, R1, next U, back 3
        # 1/8 Next R
        chance_card = (chance_card + 1) % 16
        if chance_card == 0:
            return ("GO", chance_card, chest_card)
        elif chance_card == 1:
            return ("JAIL", chance_card, chest_card)
        elif chance_card == 2:
            return ("C1", chance_card, chest_card)
        elif chance_card == 3:
            return ("E3", chance_card, chest_card)
        elif chance_card == 4:
            return ("H2", chance_card, chest_card)
        elif chance_card == 5:
            return ("R1", chance_card, chest_card)
        elif chance_card == 6:
            return (next_specific(landing_square, "U"),
                    chance_card, chest_card)
        elif chance_card == 7:
            return next_square(back(landing_square, 3),
                               chance_card, chest_card)
        elif chance_card in [8, 9]:
            return (next_specific(landing_square, "R"),
                    chance_card, chest_card)
        else:
            return (landing_square, chance_card, chest_card)
    else:
        raise Exception("Case should not occur")


def main(verbose=False):
    GAME_PLAY = 10 ** 6
    dice_size = 4
    visited = {"GO": 1}
    current = "GO"
    chance_card = 0
    chest_card = 0
    doubles = 0
    for place in xrange(GAME_PLAY):
        total, double = roll_die(dice_size)
        if double:
            doubles += 1
        else:
            doubles = 0

        if doubles == 3:
            doubles = 0
            current = "JAIL"
        else:
            index = SQUARES.index(current)
            landing_square = SQUARES[(index + total) % len(SQUARES)]
            (current, chance_card,
             chest_card) = next_square(landing_square, chance_card, chest_card)

        # if current is not in visited, sets to 1
        # (default 0 returned by get)
        visited[current] = visited.get(current, 0) + 1

    top_visited = sorted(visited.items(),
                         key=lambda pair: pair[1],
                         reverse=True)
    top_visited = [SQUARES.index(square[0]) for square in top_visited[:3]]

    return ''.join(str(index).zfill(2) for index in top_visited)

if __name__ == '__main__':
    print euler_timer(84)(main)(verbose=True)
