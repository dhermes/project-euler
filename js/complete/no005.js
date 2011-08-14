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

exports.main = function() {
    return minProduct(20);
};

if (require.main === module) {
    timer.timer(5, exports.main);
}
