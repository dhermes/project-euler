#!/usr/bin/env node

/* The first two consecutive numbers to have two distinct prime factors are:
   14 = 2 X 7, 15 = 3 X 5

   The first three consecutive numbers to have three
   distinct prime factors are:
   644 = 2^2 X 7 X 23, 645 = 3 X 5 X 43, 646 = 2 X 17 X 19

   Find the first four consecutive integers to have four distinct
   primes factors. What is the first of these numbers? */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

function increment(value, arr) {
    /**
     * This updates the value according to the list. Since we seek 4
     * consecutive numbers with exactly 4 prime factors, we can jump
     * 4 numbers if the last doesn't have 4 factors, can jump 3 if
     * the second to last doesn't have 4 factors, and so on
     */
    if (arr[arr.length - 1] != 4) {
        return value + 4;
    }

    // We can assume the last element is a 4
    if (arr[arr.length - 2] != 4) {
        return value + 3;
    }

    // We can assume the last 2 elements are [4, 4]
    if (arr[arr.length - 3] != 4) {
        return value + 2;
    }

    // We can assume the last 3 elements are [4, 4, 4]
    return value + 1;
};

exports.main = function(verbose) {
    if (typeof verbose == 'undefined') {
        verbose = false;
    }
    /* Find the first four consecutive integers to have four distinct
       primes factors. What is the first of these numbers? */
    var factorHash = {1: [], 2: [2]};
    /* Smallest product of 4 primes is 2*3*5*7 = 210
       We need to update the hash to get to this point */
    for (var i = 3; i <= 210; i++) {
        fns.primeFactors(i, false, factorHash);
    }

    var smallest = 210, // The smallest integer of the four
        numFactors = [fns.primeFactors(smallest, true, factorHash).length,
                      fns.primeFactors(smallest + 1, true, factorHash).length,
                      fns.primeFactors(smallest + 2, true, factorHash).length,
                      fns.primeFactors(smallest + 3, true, factorHash).length];

    while (!operator.arrCompare(numFactors, [4, 4, 4, 4])) {
        smallest = increment(smallest, numFactors);
        numFactors = [fns.primeFactors(smallest, true, factorHash).length,
                      fns.primeFactors(smallest + 1, true, factorHash).length,
                      fns.primeFactors(smallest + 2, true, factorHash).length,
                      fns.primeFactors(smallest + 3, true, factorHash).length];
    }

    return smallest;
};

if (require.main === module) {
    timer.timer(47, exports.main);
}
