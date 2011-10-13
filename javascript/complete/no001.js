#!/usr/bin/env node

/* If we list all the natural numbers below 10 that are multiples of 3 or 5,
   we get 3, 5, 6 and 9. The sum of these multiples is 23.

   Find the sum of all the multiples of 3 or 5 below 1000. */

var operator = require('../operator.js'),
    timer = require('../timer.js');

function filterHelper(values) {
  var result = function(n) {
    for(var i = 0, val; value = values[i]; i++) {
      if (!(n % value)) {
        return true;
      }
    }
    return false;
  };

  return result;
};

exports.main = function(verbose) {
  if (typeof verbose == 'undefined') {
    verbose = false;
  }
  var multiples = operator.range(1, 1000);
  multiples = multiples.filter(filterHelper([3, 5]));

  return operator.sum(multiples);
};

if (require.main === module) {
  timer.timer(1, exports.main);
}
