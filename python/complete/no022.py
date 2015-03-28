#!/usr/bin/env python

# Using no022.txt, a text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the
# alphabetical value for each name, multiply this value by its alphabetical
# position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN,
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 X 53 = 49714.

# What is the total of all the name scores in the file?

from python.decorators import euler_timer
from python.functions import get_data


def name_score(name):
    return sum((ord(letter.upper()) - ord('A') + 1) for letter in name)


def main(verbose=False):
    # The name file is a comma separated file with quotes
    names = sorted(get_data(22).strip('"').split('","'))
    return sum((i + 1) * name_score(name) for i, name in enumerate(names))

if __name__ == '__main__':
    print euler_timer(22)(main)(verbose=True)
