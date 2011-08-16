#!/usr/bin/env node

/* The fraction 49/98 is a curious fraction, as an inexperienced mathematician
   in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
   which is correct, is obtained by cancelling the 9s.

   We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

   There are exactly four non-trivial examples of this type of fraction, less
   than one in value, and containing two digits in the numerator and denominator.

   If the product of these four fractions is given in its lowest common
   terms, find the value of the denominator. */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

function canceledPair(numer, denom) {
    var shared = [],
        numerStr = numer.toString().split(''), 
        denomStr = denom.toString().split(''),
        numerCopy = numerStr, denomIndex;
    for (var i = 0, digit; digit = numerStr[i]; i++) {
        denomIndex = operator.inArray(digit, denomStr);
        if (denomIndex != -1 && operator.inArray(digit, shared) == -1) {
            shared.push(digit);
            denomStr = denomStr.slice(0, denomIndex).concat(denomStr.slice(denomIndex + 1));
            // Can't remove from numerStr while looping through it, use copy
            numerCopy = numerCopy.slice(0, i).concat(numerCopy.slice(i + 1));
        }
    }
    numerStr = numerCopy.length ? Number(numerCopy.join('')) : 0;
    denomStr = denomStr.length ? Number(denomStr.join('')) : 0;
    return [numerStr, denomStr];
};

function equalsCanceledPair(numer, denom) {
    var canceled = canceledPair(numer, denom),
        cNum = canceled[0], cDenom = canceled[1];
    if ((cNum == numer && cDenom == denom) || 
        (10 * cNum == numer) || (cNum == 0 && cDenom == 0)) {
       return false;
    }
    return (cNum * denom == cDenom * numer);
};

exports.main = function(verbose) {
    if (typeof verbose == 'undefined') {
        verbose = false;
    }
    var pairsNumer = [], pairsDenom = [], denom;
    for (var numer = 10; numer < 99; numer++) {
        for (denom = numer + 1; denom < 100; denom++) {
            if (equalsCanceledPair(numer, denom)) {
                pairsNumer.push(numer);
                pairsDenom.push(denom);
            }
        }
    }
    var numer = pairsNumer.reduce(operator.mul),
        denom = pairsDenom.reduce(operator.mul);
    return denom / fns.gcd(numer, denom);
};

if (require.main === module) {
    timer.timer(33, exports.main);
}
