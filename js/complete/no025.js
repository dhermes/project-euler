#!/usr/bin/env node

/* What is the first term in the Fibonacci sequence to contain 1000 digits? */

var bigint = require('bigint'),
    timer = require('../timer.js');

exports.main = function(verbose) {
    if (typeof verbose == 'undefined') {
        verbose = false;
    }
    var fibIndex = 1, last = bigint('0'), curr = bigint('1'), tmp;
    while (curr.toString().length < 1000) {
        tmp = curr.add(last);
        last = curr;
        curr = tmp;
        fibIndex++;
    }
    return fibIndex;
};

if (require.main === module) {
    timer.timer(25, exports.main);
}
