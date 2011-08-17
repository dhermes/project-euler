#!/usr/bin/env node

/* Starting with the number 1 and moving to the right in a clockwise
   direction a 5 by 5 spiral is formed as follows:

   21 22 23 24 25
   20  7  8  9 10
   19  6  1  2 11
   18  5  4  3 12
   17 16 15 14 13

   What is the sum of the numbers on the diagonals in a 1001 by 1001
   spiral formed in the same way? */

var timer = require('../timer.js');

// 1, 1, 2, 2, 3, 3, 4, 4, etc., every 2 is a corner
function spiralSum(n) {
  if (n % 2 == 0) {
    return; // Spiral only occurs on odds.
  }

  var currVal = 1, total = 0,
      /* as we move along the corners on the spiral, the number of
         steps (i.e. number of corners) dictates the size of each
         new step. In almost all cases, the step increases by one
         but every four, when the next corner wraps a new layer,
         it does not increase */
      stepNum = 0, stepSize = 0;

  while (currVal <= Math.pow(n, 2)) {
    if (stepNum % 2 == 0) {
      stepSize++;
    }
    currVal += stepSize;
    if (stepNum % 4 == 0) {
      total += currVal - 1;
    } else {
      total += currVal;
    }
    stepNum++;
  }

  return total;
};

exports.main = function(verbose) {
  if (typeof verbose == 'undefined') {
    verbose = false;
  }
  return spiralSum(1001);
};

if (require.main === module) {
  timer.timer(28, exports.main);
}
