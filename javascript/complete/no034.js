#!/usr/bin/env node

/* Find the sum of all numbers which are equal to the sum
   of the factorial of their digits.

   We know if n has d digits, then sum(n) <= d*9! = 362880d and n >= 10*(d-1)
   hence sum(n) = n implies 3628800d >= 10^d. We must have d <= 7. */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

exports.main = function(verbose) {
  if (typeof verbose == 'undefined') {
    verbose = false;
  }
  var result = [];
  /* We have at most 7 digits, so we consider all ascending
     lists of digits with a digit sum between 1 and 63.
     Since ascending requires the first element of the digit lists
     is *equal to* the minimum, we allow an 8th digit which is
     simply a padded zero */

  var sN = operator.sortNumber,
      asc, i, choice, nonZero, factorialSum,
      possibleZeros, zerosAdd, factorialDigits;
  function nonZeroFilter(val) {
    return val != 0;
  };
  for (var digitSum = 1; digitSum <= 63; digitSum++) {
    asc = fns.ascending(8, digitSum, 0, 9);
    for (i = 0; choice = asc[i]; i++) {
      choice = choice.slice(1);
      nonZero = choice.filter(nonZeroFilter);
      factorialSum = operator.sum(nonZero.map(fns.factorial));
      possibleZeros = 7 - nonZero.length;

      // Can fill out the number with zeros (up to 7 digits)
      for (zerosAdd = 0; zerosAdd <= possibleZeros; zerosAdd++) {
        factorialDigits = factorialSum.toString().split('').map(Number);
        if (operator.arrCompare(factorialDigits.sort(sN), nonZero.sort(sN))) {
          if (factorialSum > 2) {
            result.push(factorialSum);
          }
        }

        nonZero.push(0);
        factorialSum += 1; // Add factorial(0)
      }
    }
  }

  if (verbose) {
    return [operator.sum(result), '.\nThe full list of numbers is as follows: ',
            result.join(', ') , '.'].join('');
  } else {
    return operator.sum(result);
  }
};

if (require.main === module) {
  timer.timer(34, exports.main);
}
