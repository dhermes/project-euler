#!/usr/bin/env node

/* What is the sum of the digits of the number 2^(1000)? */

var bigint = require('bigint'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

exports.main = function(verbose) {
    if (typeof verbose == 'undefined') {
        verbose = false;
    }
    var power = bigint('2').pow(1000).toString(),
        digitArray = power.split('');
    return operator.sum(digitArray);
};

if (require.main === module) {
    timer.timer(16, exports.main);
}
