#!/usr/bin/env node

/* How many Sundays fell on the first of the month during
the twentieth century (1 Jan 1901 to 31 Dec 2000)?

A leap year occurs on any year evenly divisible by 4, but not
on a century unless it is divisible by 400. */

var operator = require('../operator.js'),
    timer = require('../timer.js');

function leapYear(year) {
    if (year % 4 == 0) {
        if (year % 100 == 0) {
            return (year % 400 == 0);
        } else {
            return true;
        }
    } else {
        return false
    }
};

function monthLengths(year) {
    var result = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    if (leapYear(year)) {
        result[1] = 29;
    }
    return result;
};

exports.main = function(verbose) {
    if (typeof verbose == 'undefined') {
        verbose = false;
    }
    /* We call the days of the week 0 - Sunday,...,6 - Saturday modulo 7
       1 Jan 1900 was a Monday. i.e. equal to 1 */
    var janFirst1901 = (1 + operator.sum(monthLengths(1900))) % 7,
        date = janFirst1901;

    var count = (date) ? 0 : 1, months;
    for (var year = 1901; year <= 2000; year++) {
        months = monthLengths(year);
        for (var i = 0, month; month = months[i]; i++) {
            date = (date + month) % 7;
            if (!date) {
                count++;
            }
        }
    }

    /* The final date will be Jan 1 2001, so we need to
       disallow it if it was bad */
    if (!date) {
        count -= 1;
    }

    return count;
};

if (require.main === module) {
    timer.timer(19, exports.main);
}
