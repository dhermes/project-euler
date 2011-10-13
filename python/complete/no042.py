#!/usr/bin/env python

# By converting each letter in a word to a number corresponding to
# its alphabetical position and adding these values we form a word
# value. For example, the word value for SKY is
# 19 + 11 + 25 = 55 = t_(10). If the word value is a triangle number
# then we shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'), a 16K
# text file containing nearly two-thousand common English words,
# how many are triangle words?

# I've renamed words.txt as no042.txt

import string

from python.decorators import euler_timer
from python.functions import get_data
from python.functions import reverse_polygonal_number

def word_to_value(word):
    letters = string.uppercase
    return sum([letters.find(letter) + 1 for letter in word])

def num_triangle():
    # Assumes file is "A","ABILITIY","ABLE",...
    words = get_data(42).strip('"').split('","')
    vals = [word_to_value(word) for word in words]
    triangle_hash = {}
    count = 0
    for val in vals:
        if reverse_polygonal_number(3, val, triangle_hash) != -1:
            count += 1
    return count

def main(verbose=False):
    return num_triangle()

if __name__ == '__main__':
    print euler_timer(42)(main)(verbose=True)
