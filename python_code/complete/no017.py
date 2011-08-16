#!/usr/bin/env python

# If all the numbers from 1 to 1000 (one thousand) inclusive were written
# out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
# 20 letters. The use of "and" when writing out numbers is in compliance
# with British usage.

# Assume less than or equal to 1000

from python_code.decorators import euler_timer

def words(n):
    tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty",
            7: "seventy", 8:  "eighty", 9: "ninety"}
    teens = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
             14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
             18: "eighteen", 19: "nineteen"}
    ones = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
            6: "six", 7: "seven", 8: "eight", 9: "nine"}

    if n == 1000:
        return "one thousand"

    result = []
    digs = [int(dig) for dig in str(n).zfill(3)]

    if digs[0] != 0:
        if n != 100*digs[0]:
            result.extend([ones[digs[0]] , "hundred", "and"])
        else:
            return "%s hundred" % ones[digs[0]]

    if digs[1] == 1:
        result.append(teens[10*digs[1] + digs[2]])
        return " ".join(result)
    elif digs[1] != 0:
        result.append(tens[digs[1]])

    # Here we can safely ignore teens since we return in that loop
    if digs[2] != 0:
        result.append(ones[digs[2]])

    return " ".join(result)

def num_letters_in_word(n):
    result = words(n)
    result = "".join(result.split())
    result = "".join(result.split("-"))
    return len(result)

def main(verbose=False):
    return sum([num_letters_in_word(i) for i in range(1, 1001)])

if __name__ == '__main__':
    print euler_timer(17)(main)(verbose=True)
