#!/usr/bin/env node

/* There exists exactly one Pythagorean triplet for which
   a + b + c = 1000. Find the product abc. */

var operator = require('../operator.js'),
    timer = require('../timer.js');

function firstTriplet(total) {
  var c;
  for(var a = 1; a < total - 1; a++) {
    for(var b = 1; b < total - a; b++) {
      c = total - a - b;
      if(a * a + b * b == c * c) {
        return [a, b, c];
      }
    }
  }

  return []; // None found
};

exports.main = function(verbose) {
  if (typeof verbose == 'undefined') {
    verbose = false;
  }
  var triplet = firstTriplet(1000),
      result = triplet.reduce(operator.mul, 1);
  return result;
};

if (require.main === module) {
  timer.timer(9, exports.main);
}
