#!/usr/bin/env python

from math import sqrt

from python.decorators import euler_timer
from python.functions import get_data


def same_signature(n, word):
    digits = [dig for dig in str(n)]
    dig_set = set(digits)
    letter_set = set(word)
    if len(dig_set) != len(letter_set):
        return (False, None)

    first_found = [word.find(letter) for letter in letter_set]
    translated = word
    for index in first_found:
        translated = translated.replace(word[index], digits[index])

    if translated == str(n):
        return (True, [(word[index], digits[index]) for index
                       in first_found])
    else:
        return (False, None)


def strings_by_length(data):
    result = {}
    for val in data:
        length = len(str(val))
        # sets value to [] if not set, returns value at key
        result.setdefault(length, []).append(val)
    return result


def main(verbose=False):
    data = get_data(98)[1:-1].split('","')
    words = strings_by_length(data)

    max_len = int(sqrt(10) ** max(words))
    squares = strings_by_length(
        [i ** 2 for i in range(1, int(sqrt(10) ** max(words)))])

    max_val = 0
    for word_length in sorted(words.keys())[::-1]:
        total_words = len(words[word_length])
        for first in range(total_words - 1):
            for second in range(first + 1, total_words):
                first_word = words[word_length][first]
                second_word = words[word_length][second]
                # check anagrams
                if sorted(first_word) == sorted(second_word):
                    for square in squares[word_length]:
                        val, translation = same_signature(square, first_word)
                        if val:
                            translated = second_word
                            for letter, digit in translation:
                                translated = translated.replace(letter, digit)
                            new_number = int(translated)
                            if new_number in squares[word_length]:
                                to_add = max(square, new_number)
                                if to_add > max_val:
                                    max_val = to_add
        if max_val > 0:
            return max_val
    raise Exception("Program failed to find solution")

if __name__ == '__main__':
    print euler_timer(98)(main)(verbose=True)
