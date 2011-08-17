#!/usr/bin/env node

/* A number n is called abundant if the sum of its proper divisors exceeds n.

   By mathematical analysis, it can be shown that all integers greater than
   28123 can be written as the sum of two abundant numbers.

   Find the sum of all the positive integers which cannot be written as
   the sum of two abundant numbers. */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

function abundantNumbers(n) {
  var factorHash = fns.allFactors(n),
      // sum of proper divisors
      result = [];
  for (var i = 2; i <= n; i++) {
    if (i < operator.sum(factorHash[i]) - i) {
      result.push(i);
    }
  }
  return result;
};

// Array size limit is 4294967295 or 2^32 - 1
// http://4umi.com/web/javascript/array.php
exports.main = function(verbose) {
  if (typeof verbose == 'undefined') {
    verbose = false;
  }
  var abundants = abundantNumbers(28123);

  // Had to break from python implementation because of memory considerations,
  // as a result, the algo is better
  var sums = {}, i, val1, j, val2;
  for (var i = 0; i <= 28123; i++) {
    sums[i] = false;
  }

  for (i = 0; val1 = abundants[i]; i++) {
    for (j = i; val2 = abundants[j]; j++) {
        if (val1 + val2 <= 28123) {
          sums[val1 + val2] = true;
        }
    }
  }

  var badOnes = [];
  for (var i = 0; i <= 28123; i++) {
    if (!sums[i]) {
      badOnes.push(i);
    }
  }

  return operator.sum(badOnes);
};

if (require.main === module) {
  timer.timer(23, exports.main);
}
