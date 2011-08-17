#!/usr/bin/env node

/* The number, 1406357289, is a 0 to 9 pandigital number because it is made up
   of each of the digits 0 to 9 in some order, but it also has a rather
   interesting sub-string divisibility property.

   Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we
   note the following:

   d_2 d_3 d_4 = 406 is divisible by 2
   d_3 d_4 d_5 = 063 is divisible by 3
   d_4 d_5 d_6 = 635 is divisible by 5
   d_5 d_6 d_7 = 357 is divisible by 7
   d_6 d_7 d_8 = 572 is divisible by 11
   d_7 d_8 d_9 = 728 is divisible by 13
   d_8 d_9 d_10 = 289 is divisible by 17

   Find the sum of all 0 to 9 pandigital numbers with this property.

   Since 5 | d_4 d_5 d_6, we know d_6 in [0,5]
   Since 11 | d_6 d_7 d_8 in [0 d_7 d_8, 5 d_7, d_8], we know d_6 = 5
   This is because the only multiples of 11 with d_6 = 0 are
   11, 22, ..., 99, all of which have repeated digits
   11*50 = 550 is also eliminated, leaving us with
   d_6 d_7 d_8 in [506, 517, 528, 539, 561, 572, 583, 594] */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

function extendMatches(value, choices, direction) {
  /**
   * Extends the value by anything in choices the
   * 1) ends in the same 2 digits that value begins with
   * 2) has remaining digit(s) unique from those in value
   */
  var valueDigits = operator.uniqSorted(value.split('')), matches;
  if (direction == 'right') {
    function firstTwoFilter(choice) {
      return (choice.slice(0, 2) == value.slice(-2));
    };
    var firstTwoMatch = choices.filter(firstTwoFilter);
    function noIntersectFilterLast(choice) {
      for (var i = 2; i < choice.length; i++) {
        if (operator.inArray(choice[i], valueDigits) != -1) {
          return false;
        }
      }
      return true;
    };
    matches = firstTwoMatch.filter(noIntersectFilterLast);
    function preAddMap(choice) {
      return value + choice.slice(2);
    };
    return matches.map(preAddMap);
  } else if (direction == 'left') {
    function lastTwoFilter(choice) {
      return (choice.slice(-2) == value.slice(0, 2));
    };
    var lastTwoMatch = choices.filter(lastTwoFilter);
    function noIntersectFilterFirst(choice) {
      for (var i = 0; i < choice.length - 2; i++) {
        if (operator.inArray(choice[i], valueDigits) != -1) {
          return false;
        }
      }
      return true;
    };
    matches = lastTwoMatch.filter(noIntersectFilterFirst);
    function postAddMap(choice) {
      return choice.slice(0, -2) + value;
    };
    return matches.map(postAddMap);
  } else {
    return; // (direction) not a valid direction.
  }
};

function extendToRemainingDigit(value) {
  // value assumed to be string
  var lastDigit = [];
  for (var i = 0; i < 10; i++) {
    if (operator.inArray(i, value) == -1) {
       lastDigit.push(i);
    }
  }

  if (lastDigit.length != 1) {
    return; // Algorithm for 43 failed.
  }

  lastDigit = lastDigit[0];
  return Number(lastDigit + value);
};

exports.main = function(verbose) {
  if (typeof verbose == 'undefined') {
    verbose = false;
  }
  var uniqueDigits = {},
      primes = [2, 3, 5, 7, 11, 13, 17], mults;

  function primeFilter(prime) {
    var result = function(number) {
      return (number % prime == 0);
    }
    return result;
  };

  function padMap(number) {
    return fns.zeroPad(number, 3);
  };

  function threeDigitsUniqueFilter(number) {
    return (operator.uniqSorted(number.split('')).length == 3);
  };

  var allVals = operator.range(1, 1000);
  for (var i = 0, prime; prime = primes[i]; i++) {
    mults = allVals.filter(primeFilter(prime)).map(padMap);
    uniqueDigits[prime] = mults.filter(threeDigitsUniqueFilter);
  }
  function firstDigitFive(number) {
    return (number[0] == '5');
  };
  var candidates = uniqueDigits[11].filter(firstDigitFive);

  /* We have only covered the 11 case, so we need to include those for the
     13 and 17 to the right and 7, 5, 3, 2 to the left (in order) */
  function mapPrime(prime, direction) {
    var result = function(candidate) {
      return extendMatches(candidate, uniqueDigits[prime], direction);
    }
    return result;
  };

  primes = [13, 17];
  for (i = 0, prime; prime = primes[i]; i++) {
    candidates = candidates.map(mapPrime(prime, 'right')).reduce(operator.arrAdd);
  }

  primes = [7, 5, 3, 2];
  for (i = 0, prime; prime = primes[i]; i++) {
    candidates = candidates.map(mapPrime(prime, 'left')).reduce(operator.arrAdd);
  }

  /* We now have all possibilities for d_2 ... d_10, from which we can
     generate d_1 */
  candidates = candidates.map(extendToRemainingDigit);
  return operator.sum(candidates);
};

if (require.main === module) {
  timer.timer(43, exports.main);
}
