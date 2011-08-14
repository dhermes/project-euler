#!/usr/bin/env node

/* The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
   increases by 3330, is unusual in two ways: (i) each of the three
   terms are prime, and, (ii) each of the 4-digit numbers are
   permutations of one another.

   There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
   primes, exhibiting this property, but there is one other 4-digit
   increasing sequence.

   What 12-digit number do you form by concatenating the three terms
   in this sequence? */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

function findArithmetic(arr) {
    if (arr.length < 3) {
        return; // List wrong size.
    }

    var candidates = fns.allSubsets(arr, 3);
    for (var i = 0, cand; cand = candidates[i]; i++) {
        if (cand[0] + cand[2] == 2 * cand[1]) {
            return cand;
        }
    }
    return [];
};

exports.main = function() {
    function geValFilter(val) {
        var result = function(number) {
            return number > val;
        };
        return result;
    };
    var primes = fns.sieve(10000).filter(geValFilter(999)),
        primesByDigits = {}, key;
    for (var i = 0, prime; prime = primes[i]; i++) {
        key = prime.toString().split('').sort().join(''); //
        if (key in primesByDigits) {
            primesByDigits[key].push(prime);
        } else {
            primesByDigits[key] = [prime];
        }
    }

    var result = [], candidate, soln;
    for (key in primesByDigits) {
        candidate = primesByDigits[key];
        if (candidate.length > 2) {
            soln = findArithmetic(candidate);
            if (soln.length) {
                result.push(operator.uniqSorted(soln).join(''));
            }
        }
    }
    return result[0]; // No solution found
};

if (require.main === module) {
    timer.timer(49, exports.main);
}
