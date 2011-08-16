#!/usr/bin/env node

/* If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance
with British usage.

Assume less than or equal to 1000 */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

function words(n) {
    var tens = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
                7: 'seventy', 8:  'eighty', 9: 'ninety'},
        teens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
                 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
                 18: 'eighteen', 19: 'nineteen'},
        ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'};
    if (n == 1000) {
        return 'one thousand';
    }

    var result = [], digs = fns.zeroPad(n, 3).split('');

    if (digs[0] != '0') {
        if (n != 100 * parseInt(digs[0])) {
            result = result.concat([ones[digs[0]], 'hundred', 'and']);
        } else {
            return ones[digs[0]] + ' hundred';
        }
    }

    if (digs[1] == '1') {
        result.push(teens[10 * parseInt(digs[1]) + parseInt(digs[2])]);
        return result.join(' ');
    } else if (digs[1] != '0') {
        result.push(tens[digs[1]]);
    }

    // Here we can safely ignore teens since we return in that loop
    if (digs[2] != '0') {
        result.push(ones[digs[2]]);
    }

    return result.join(' ');
};

function numLettersInWord(n) {
    var result = words(n);

    function spaceHyphenFilter(str) {
        return (str != ' ' && str != '-');
    };    

    // Filter out all with space or hyphens
    result = result.split('').filter(spaceHyphenFilter).join('');
    return result.length;
};

exports.main = function(verbose) {
    if (typeof verbose == 'undefined') {
        verbose = false;
    }
    return operator.sum(operator.range(1, 1001).map(numLettersInWord));
};

if (require.main === module) {
    timer.timer(17, exports.main);
}
