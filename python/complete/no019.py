#!/usr/bin/env python

# How many Sundays fell on the first of the month during
# the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# A leap year occurs on any year evenly divisible by 4, but not
# on a century unless it is divisible by 400.

from python.decorators import euler_timer


def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True
    else:
        return False


def month_lengths(year):
    result = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year(year):
        result[1] = 29
    return result


def main(verbose=False):
    # We call the days of the week 0 - Sunday,...,6 - Saturday modulo 7
    # 1 Jan 1900 was a Monday. i.e. equal to 1
    jan_1_1901 = (1 + sum(month_lengths(1900))) % 7

    date = jan_1_1901
    count = 0 if date else 1
    for year in range(1901, 2001):
        months = month_lengths(year)
        for month in months:
            date = (date + month) % 7
            if date == 0:
                count += 1

    # The final date will be Jan 1 2001, so we need to
    # disallow it if it was bad
    if date == 0:
        count -= 1
    return count

if __name__ == '__main__':
    print euler_timer(19)(main)(verbose=True)
