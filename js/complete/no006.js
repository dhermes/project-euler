#!/usr/bin/env node

/* Find the difference between the sum of the squares of the
   first one hundred natural numbers and the square of the sum */

var fns = require('../functions.js'),
    timer = require('../timer.js');

function sumFirstNSq(n) {
    return n * (n + 1) * (2 * n + 1) / 6;
};

function main() {
    return Math.abs(sumFirstNSq(100) - Math.pow(fns.polygonalNumber(3, 100), 2));
};

timer.timer(6, main);
