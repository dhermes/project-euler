#!/usr/bin/env node

/* The number 3797 has an interesting property. Being prime itself,
   it is possible to continuously remove digits from left to right,
   and remain prime at each stage:
   3797, 797, 97, and 7.

   Similarly we can work from right to left: 3797, 379, 37, and 3.

   Find the sum of the only eleven primes that are both truncatable from
   left to right and right to left.

   NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes. */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

function truncatedList(n, fromLeft) {
  function numJoinMap(arr) {
    return Number(arr.join(''));
  };

  var digs = n.toString().split('');
  if (fromLeft) {
    function subMapLeft(i) {
      return digs.slice(i);
    };
    return operator.range(digs.length).map(subMapLeft).map(numJoinMap);
  } else {
    // If the bool fromLeft is false, we are right
    function subMapRight(i) {
      return digs.slice(0, i + 1);
    };
    return operator.range(digs.length).map(subMapRight).map(numJoinMap);
  }
};

function truncatedAll(n) {
  var result = truncatedList(n, true).concat(truncatedList(n, false));
  return operator.uniq(result);
};

function isTruncatablePrime(n, primes) {
  var candidates = truncatedAll(n);
  for (var i = 0, candidate; candidate = candidates[i]; i++) {
    if (operator.inArray(candidate, primes) != -1) {
      continue;
    } else if (fns.isPrime(candidate)) {
      primes.push(candidate);
    } else {
      return false;
    }
  }
  return true;
};

function findFirstNTruncatable(n, maxN) {
  var result = [],
      // We don't include 2, 3, 5, or 7
      primes = fns.sieve(maxN).slice(4);
  for (var i = 0, prime; prime = primes[i]; i++) {
    if (isTruncatablePrime(prime, primes)) {
      result.push(prime);
    }

    if (result.length == n) {
      return result;
    }
  }

  if (result.length < n) {
    return; // Not enough found, raise maxN
  }
  return result;
};

exports.main = function(verbose) {
  if (typeof verbose == 'undefined') {
    verbose = false;
  }
  var ans = findFirstNTruncatable(11, Math.pow(10, 6));

  if (verbose) {
    return [operator.sum(ans), '.\nThe primes are: ',
            ans.join(', '), '.'].join('');
  } else {
    return operator.sum(ans);
  }
};

if (require.main === module) {
  timer.timer(37, exports.main);
}
