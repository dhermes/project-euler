#!/usr/bin/env node

/* What is the smallest positive number that is evenly
   divisible by all of the numbers from 1 to 20? */

var fns = require('../functions.js'),
    timer = require('../timer.js');

function minProduct(n) {
    if (n < 2) {
        return 1;
    }

    var product = minProduct(n - 1),
        sharedFactors = fns.gcd(product, n);
    return (product * n) / sharedFactors;
};

function main() {
    return minProduct(20);
};

timer.timer(5, main);
