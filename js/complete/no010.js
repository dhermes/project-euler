#!/usr/bin/env node

/* Find the sum of all the primes below two million. */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

exports.main = function(verbose) {
  if (typeof verbose == 'undefined') {
    verbose = false;
  }
  var primes = fns.sieve(2000000),
      result = operator.sum(primes);
  return result;
};

if (require.main === module) {
  timer.timer(10, exports.main);
}
