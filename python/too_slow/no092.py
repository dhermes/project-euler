#!/usr/bin/env python

from python.decorators import euler_timer


def main(verbose=False):
    destinations = {1: 1, 89: 89}
    count = 1  # 89 has already been encountered
    for i in range(2, 10 ** 7):
        curr = i
        to_add = []
        while curr not in destinations:
            to_add.append(curr)
            curr = sum(int(digit) ** 2 for digit in str(curr))

        # now curr will be in destinations
        value = destinations[curr]
        for elt in to_add:
            if elt < 10 ** 7 and value == 89:
                count += 1
            destinations[elt] = value

    return count

if __name__ == '__main__':
    print euler_timer(92)(main)(verbose=True)
