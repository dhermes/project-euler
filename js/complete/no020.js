#!/usr/bin/env node

/* Find the sum of the digits in the number 100! */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

function main() {
    // Sum will cast to Number
    return operator.sum(fns.factorial(100, true).split(''));
};

timer.timer(20, main);
