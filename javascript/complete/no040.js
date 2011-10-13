#!/usr/bin/env node

/* An irrational decimal fraction is created by concatenating
   the positive integers:
   0.123456789101112131415161718192021...

   It can be seen that the 12th digit of the fractional part is 1.

   If d_n represents the nth digit of the fractional part, find the
   value of the following expression.
   d_1 X d_10 X d_100 X d_1000 X d_10000 X d_100000 X d_1000000 */

var operator = require('../operator.js'),
    timer = require('../timer.js');

function numDigsWithUpToDDigits(d) {
  /* The smallest number with d + 1 digits is 10**d
     S = sum_(i = 1)^d i*9*10**(i - 1) = 0.9 * sum_(i = 1)^d i 10**i
     10S - S = 0.9 sum_(i = 1)^d i 10**(i + 1) - 0.9 sum_(i = 1)^d i 10**i
     10S = sum_(i = 2)^(d + 1) (i - 1) 10**i - sum_(i = 1)^d i 10**i
     10S = d*10**(d + 1) - sum_(i = 1)^d 10**i
     90S = 9*d*10**(d + 1) - 10**(d + 1) + 10
     9S = (9*d - 1)*10**d + 1 */
  return ((9 * d - 1) * Math.pow(10, d) + 1) / 9;
};

function nthDigitOfFracPart(n) {
  var numDigits = 1;
  while (numDigsWithUpToDDigits(numDigits) < n) {
    numDigits++;
  }

  /* We know the nth digit occurs in the block of integers with num_digits
     digits. We want to determine which digit in the block it is */
  var placeInDigits = n - numDigsWithUpToDDigits(numDigits - 1),
      digitPlaceInNumber = ((placeInDigits - 1) % numDigits) + 1,
      numbersPrior = Math.floor((placeInDigits - 1) / numDigits);

  /* Since there are numbers_prior numbers of num_digits digits prior to
     the number we are interested in, we need to calculate which number it is
     The smallest number with num_digits digits is 10**(num_digits - 1) */
  var numOfInterest = (Math.pow(10, numDigits - 1) + numbersPrior).toString();
  return Number(numOfInterest[digitPlaceInNumber - 1]);
};

exports.main = function(verbose) {
  // d_1 X d_10 X d_100 X d_1000 X d_10000 X d_100000 X d_1000000
  if (typeof verbose == 'undefined') {
      verbose = false;
  }
  function mapPower10(exponent) {
    return Math.pow(10, exponent);
  };
  var result = operator.range(7).map(mapPower10).map(nthDigitOfFracPart),
      digitDisplay = [];
  for (var i = 0, digit; digit = result[i]; i++) {
    digitDisplay.push('d_' + Math.pow(10, i) + ' = ' + digit);
  }

  if (verbose) {
    return [result.reduce(operator.mul), '.\nThe digits are as follows: ',
            digitDisplay.join(', '), '.'].join('');
  } else {
    return result.reduce(operator.mul);
  }
};

if (require.main === module) {
  timer.timer(40, exports.main);
}
