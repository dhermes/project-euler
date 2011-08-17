#!/usr/bin/env node

/* What is the smallest odd composite n that can't be written n = p + 2k^2
   for some prime p and some integer k? */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

function isPossible(n, primes) {
  if (n % 2 == 0 || operator.inArray(n, primes) != -1) {
    return; // Value poorly specified
  }

  function valFilter(val) {
    var result = function(number) {
      return (number < val & number != 2);
    };
    return result;
  };
  var primesLess = primes.filter(valFilter(n));
  for (var i = 0, prime; prime = primesLess[i]; i++) {
    if (fns.isPower((n - prime) / 2, 2)) {
      return true;
    }
  }
  return false;
};

exports.main = function(verbose) {
  if (typeof verbose == 'undefined') {
    verbose = false;
  }
  // sieve(6000) will do it (answer is 5777)
  var curr = 9,
      primes = fns.sieve(5777);
  while (isPossible(curr, primes)) {
    curr += 2;
    while (operator.inArray(curr, primes) != -1) {
      curr += 2;
    }
  }
  return curr;
};

if (require.main === module) {
  timer.timer(46, exports.main);
}
