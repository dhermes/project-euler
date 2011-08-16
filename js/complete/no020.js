#!/usr/bin/env node

/* Find the sum of the digits in the number 100! */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

exports.main = function(verbose) {
    if (typeof verbose == 'undefined') {
        verbose = false;
    }
    // Sum will cast to Number
    return operator.sum(fns.factorial(100, true).split(''));
};

if (require.main === module) {
    timer.timer(20, exports.main);
}
