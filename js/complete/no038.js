#!/usr/bin/env node

/* What is the largest 1 to 9 pandigital 9-digit number that can be formed as
   the concatenated product of an integer with (1,2, ... , n) where n > 1? */

var operator = require('../operator.js'),
    timer = require('../timer.js');

function isPandigitalNine(str) {
    for (var dig = 1; dig < 10; dig++) {
        if (str.split(dig).length != 2) { // more or less than 1 occurence
            return false;
        }
    }
    return true;
};

function allPandigitals1ToN(n) {
    var toMult = operator.range(1, n + 1), multiplier = 1, result = [];

    function multipleMap(multiplier) {
        var result = function(elt) {
            return multiplier * elt;
        };
        return result;
    };

    var curr = toMult.map(multipleMap(multiplier)).join('');
    while (curr.length < 10) {
        if (isPandigitalNine(curr)) {
            result.push(curr);
        }
        multiplier++;
        curr = toMult.map(multipleMap(multiplier)).join('');
    }

    return result;
};

exports.main = function() {
    var result = [];
    for (var n = 2; n < 10; n++) {
        result = result.concat(allPandigitals1ToN(n));
    }
    return Math.max.apply(Math, result.map(Number));
};

if (require.main === module) {
    timer.timer(38, exports.main);
}
