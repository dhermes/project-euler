from math import sqrt

from python_code.functions import get_data
from python_code.functions import all_subsets

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

data = get_data(98)[1:-1].split('","')

words = {}
for word in data:
    length = len(word)
    if length in words:
        words[length].append(word)
    else:
        words[length] = [word]

max_len = int(sqrt(10)**max(words))
squares = {}
for i in range(1, max_len):
    square = i**2
    length = len(str(square))
    if length in squares:
        squares[length].append(square)
    else:
        squares[length] = [square]

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
        break
print max_val
