#!/usr/bin/env node

/* The prime 41, can be written as the sum of six consecutive primes:
   41 = 2 + 3 + 5 + 7 + 11 + 13

   This is the longest sum of consecutive primes that adds to a prime
   below one-hundred.

   The longest sum of consecutive primes below one-thousand that adds
   to a prime, contains 21 terms, and is equal to 953.

   Which prime, below one-million, can be written as the sum of the
   most consecutive primes? */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

function maxPrimeLength(digits, primes) {
  /**
   * Returns the length of the longest string of primes
   * (starting at 2,3,5,...) that will sum to less 10**digits
   */
  if (typeof primes == 'undefined') {
    primes = [];
  }
  var cap = Math.pow(10, digits);
  if (primes.length == 0) {
    primes = fns.sieve(Math.floor(4 * Math.sqrt(cap)));
  }
  var count = 0, numPrimes = 0;
  for (var i = 0, prime; prime = primes[i]; i++) {
    if (count + prime < cap) {
      count += prime;
      numPrimes++;
    } else {
      return numPrimes;
    }
  }
  return; // maxPrimeLength failed logic.
};

function allPrimeSeqs(length, digits, primes) {
  /**
   * Returns all sequences of primes of
   *
   * Assumes length <= max_prime_length(digits)
   */
  if (typeof primes == 'undefined') {
    primes = [];
  }

  var cap = Math.pow(10, digits);
  if (primes.length == 0) {
    primes = fns.sieve(cap);
  }

  var result = [], finalIndex = length - 1,
      curr = primes.slice(finalIndex - length + 1, finalIndex + 1),
      runningSum = operator.sum(curr);
  while (runningSum < cap) {
    runningSum -= curr[0]; // remove the smallest value from the sum
    result.push(curr);
    finalIndex++;
    curr = primes.slice(finalIndex - length + 1, finalIndex + 1),
    runningSum += curr[curr.length - 1]; // add the new largest
  }
  return result;
};

function primeSequenceExists(length, digits, primes) {
  /**
   * Returns True if a sequence of length consecutive primes which sums
   * to less than 10**digits also sums to a prime number
   */
  if (typeof primes == 'undefined') {
    primes = [];
  }

  var cap = Math.pow(10, digits);
  if (primes.length == 0) {
    primes = fns.sieve(cap);
  }
  var sums = allPrimeSeqs(length, digits, primes).map(operator.sum);
  for (var i = 0, sum; sum = sums[i]; i++) {
    if (operator.inArray(sum, primes) != -1) {
      return true;
    }
  }
  return false;
};

function longestPrimeSequence(digits, primes) {
  /**
   * Returns the length of the most consecutive primes which sum
   * to a prime and sum to less then 10**digits
   */
  if (typeof primes == 'undefined') {
    primes = [];
  }

  if (primes.length == 0) {
    primes = fns.sieve(Math.pow(10, digits));
  }
  var maxLength = maxPrimeLength(digits, primes);
  for (var length = maxLength; length > 0; length--) {
    if (primeSequenceExists(length, digits, primes)) {
      return length;
    }
  }

  return; // Algorithm failed
};

function longestPrime(digits) {
  var primes = fns.sieve(Math.pow(10, digits)),
      length = longestPrimeSequence(digits, primes),
      sums = allPrimeSeqs(length, digits, primes).map(operator.sum),
      intersect = [];

  for (var i = 0, sum; sum = sums[i]; i++) {
    if (operator.inArray(sum, primes) != -1) {
      intersect.push(sum);
    }
  }
  return Math.max.apply(Math, intersect);
};

exports.main = function(verbose) {
  if (typeof verbose == 'undefined') {
    verbose = false;
  }
  return longestPrime(6);
};

if (require.main === module) {
  timer.timer(50, exports.main);
}
