#!/usr/bin/env node

/* What is the largest prime factor of the number 600851475143 */

var fns = require('../functions.js'),
    timer = require('../timer.js');

exports.main = function(verbose) {
    if (typeof verbose == 'undefined') {
        verbose = false;
    }
    return Math.max.apply(Math, fns.primeFactors(600851475143));
};

if (require.main === module) {
    timer.timer(3, exports.main);
}
