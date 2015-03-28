#!/usr/bin/env python

# High Card - 1
# One Pair - 2
# Two Pairs - 3
# Three of a Kind - 4
# Straight - 5
# Flush - 6
# Full House - 7
# Four of a Kind - 8
# Straight Flush - 9
# Royal Flush - 10

# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace

# The file, no054.txt, contains one-thousand random hands dealt to two players.
# Each line of the file contains ten cards (separated by a single space): the
# first five are Player 1's cards and the last five are Player 2's cards. You
# can assume that all hands are valid (no invalid characters or repeated
# cards), each player's hand is in no specific order, and in each hand there
# is a clear winner.

# Example Row in File
# 7C 3C TH 5S 8H 8C 9C JD TC KD

from python.decorators import euler_timer
from python.functions import get_data

CARDS = dict([('2', 2),
              ('3', 3),
              ('4', 4),
              ('5', 5),
              ('6', 6),
              ('7', 7),
              ('8', 8),
              ('9', 9),
              ('T', 10),
              ('J', 11),
              ('Q', 12),
              ('K', 13),
              ('A', 14)])


def read_card(card_from_file):
    value, suit = card_from_file
    return (CARDS[value], suit)


def read_hand(hand_from_file):
    cards = [card.strip() for card in hand_from_file.split() if card]
    player1 = [read_card(card) for card in cards[:5]]
    player2 = [read_card(card) for card in cards[5:]]
    return (player1, player2)


def is_straight(hand):
    values = sorted(card[0] for card in hand)
    smallest = values[0]
    values = [value - smallest for value in values]
    return values == range(5)


def is_flush(hand):
    return (len(set(card[1] for card in hand)) == 1)


def is_royal(hand):
    return (min(card[0] for card in hand) >= 10)


def top_cards(hand):
    royal = is_royal(hand)
    straight = is_straight(hand)
    flush = is_flush(hand)
    if royal and flush:
        return (10, hand, [])
    if straight:
        if flush:
            return (9, hand, [])
        else:
            return (5, hand, [])
    else:
        if flush:
            return (6, hand, [])
    values = [card[0] for card in hand]
    num_cards = len(set(values))
    if num_cards == 2:
        val1, val2 = set(values)
        counts = sorted((values.count(val1), values.count(val2)))
        if counts == [2, 3]:
            return (7, hand, [])
        elif counts == [1, 4]:
            if values.count(val1) == 4:
                winner = val1
            else:
                winner = val2
            quad = [card for card in hand if card[0] == winner]
            kicker = [card for card in hand if card[0] != winner]
            return (8, quad, kicker)
    elif num_cards == 3:
        val1, val2, val3 = set(values)
        counts = sorted((values.count(val1),
                         values.count(val2),
                         values.count(val3)))
        if counts == [1, 2, 2]:
            if values.count(val1) == 1:
                loser = val1
            elif values.count(val2) == 1:
                loser = val2
            else:
                loser = val3
            pairs = [card for card in hand if card[0] != loser]
            kicker = [card for card in hand if card[0] == loser]
            return (3, pairs, kicker)
        elif counts == [1, 1, 3]:
            if values.count(val1) == 3:
                winner = val1
            elif values.count(val2) == 3:
                winner = val2
            else:
                winner = val3
            trips = [card for card in hand if card[0] == winner]
            kickers = [card for card in hand if card[0] != winner]
            kickers = sorted(kickers, key=lambda card: card[0])
            return (4, trips, kickers)
    elif num_cards == 4:
        for card in hand:
            if values.count(card[0]) == 2:
                winner = card[0]
                break
        pairs = [card for card in hand if card[0] == winner]
        kickers = [card for card in hand if card[0] != winner]
        kickers = sorted(kickers, key=lambda card: card[0])
        return (2, pairs, kickers)
    else:
        winner = max(values)
        high = [card for card in hand if card[0] == winner]
        kickers = [card for card in hand if card[0] != winner]
        kickers = sorted(kickers, key=lambda card: card[0])
        return (1, high, kickers)
    raise Exception(hand)


def compare_kickers(kicker1, kicker2):
    # assumes they are the same
    if len(kicker1) != len(kicker2):
        raise Exception("Dan dumb")

    num_cards = len(kicker1)
    for i in range(num_cards - 1, -1, -1):
        if kicker1[i] > kicker2[i]:
            return 1
        elif kicker1[i] < kicker2[i]:
            return 2
    raise Exception("Dan dumb 2")
    return


def compare_hands(hand1, hand2):
    if hand1[0] < hand2[0]:
        return 2
    elif hand1[0] > hand2[0]:
        return 1

    hand_value = hand1[0]
    if hand_value in (1, 2, 4, 8):
        if hand1[1][0][0] > hand2[1][0][0]:
            return 1
        elif hand1[1][0][0] < hand2[1][0][0]:
            return 2
        else:
            return compare_kickers(hand1[2], hand2[2])
    elif hand_value in (3, 7):
        vals1 = sorted(list(set(card[0] for card in hand1[1])))
        vals2 = sorted(list(set(card[0] for card in hand2[1])))
        if vals1[1] > vals2[1]:
            return 1
        if vals1[1] < vals2[1]:
            return 2
        else:
            if vals1[0] > vals2[0]:
                return 1
            if vals1[0] < vals2[0]:
                return 2
            else:
                return compare_kickers(hand1[2], hand2[2])
    elif hand_value == 5:
        max1 = max(card[0] for card in hand1[1])
        max2 = max(card[0] for card in hand2[1])
        if max1 > max2:
            return 1
        elif max1 < max2:
            return 2
        else:
            raise Exception("Dan bad 3")
    else:
        raise Exception("Dan bad 4")
    raise Exception("Dan bad 5")
    return


def main(verbose=False):
    data = get_data(54)
    hands = [read_hand(row) for row in data.split("\n") if row]
    hands = [(top_cards(entry[0]), top_cards(entry[1])) for entry in hands]

    count = 0
    for hand in hands:
        if compare_hands(*hand) == 1:
            count += 1
    return count

if __name__ == '__main__':
    print euler_timer(54)(main)(verbose=True)
