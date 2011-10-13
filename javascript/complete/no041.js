#!/usr/bin/env node

/* We shall say that an n-digit number is pandigital if it makes use of all
   the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
   and is also prime.

   What is the largest n-digit pandigital prime that exists? */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

// This is marked too slow because the worst case (8 digits), has
// an array of size 40320 and takes forever
exports.main = function(verbose) {
  if (typeof verbose == 'undefined') {
    verbose = false;
  }
  var maxN = 987654321, primes = fns.sieve(Math.floor(Math.sqrt(maxN))),
      cand, candidate, candidates, j;
  /* A 9 digit pandigital will have digit sum 45, so can't be prime
     must be divisible by 9 */
  for (var i = 8; i > 1; i--) {
    cand = Number(operator.range(1, i + 1).join(''));
    candidates = operator.uniq(fns.allPermutationsDigits(cand)).reverse();
    for (j = 0; candidate = candidates[j]; j++) {
      if (fns.isPrime(candidate, primes, maxN)) {
        return candidate;
      }
    }
  }
  return; // No prime was found, algorithm busted
};

if (require.main === module) {
  timer.timer(41, exports.main);
}
