#!/usr/bin/env node

/* Find the greatest product of five consecutive
   digits in the 1000-digit number. */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

function productConsecDigits(number, consecutive) {
    /* Returns the largest product of 'consecutive'
       consecutive digits from number */
    var digits = number.toString().split(''),
        maxStart = digits.length - consecutive,
        result = [];

    /* Could track the product instead of reducing each time.
       Just doing what python does. */
    for (var i = 0; i < maxStart + 1; i++) {
	result.push(digits.slice(i, i + consecutive).reduce(operator.mul, 1));
    }

    return result;
};

exports.main = function(verbose) {
    if (typeof verbose == 'undefined') {
        verbose = false;
    }
    var data = fns.getData(8).split('\n').join(''),
        products = productConsecDigits(data, 5);
    return Math.max.apply(Math, products);
};

if (require.main === module) {
    timer.timer(8, exports.main);
}
