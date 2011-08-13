#!/usr/bin/env node

/* What is the sum of the digits of the number 2^(1000)? */

var bigint = require('bigint'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

function main() {
    var power = bigint('2').pow(1000).toString(),
        digitArray = power.split('');
    return operator.sum(digitArray);
};

timer.timer(16, main);
