#!/usr/local/bin/node

/* What is the largest prime factor of the number 600851475143 */

var fns = require('../functions.js'),
    timer = require('../timer.js');

function main() {
    return Math.max.apply(Math, fns.primeFactors(600851475143));
};

timer.timer(3, main);
