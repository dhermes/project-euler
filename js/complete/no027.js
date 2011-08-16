#!/usr/bin/env node

/* Using computers, the incredible formula  n^2 + 79n + 1601 was discovered,
   which produces 80 primes for the consecutive values n = 0 to 79. The
   product of the coefficients, 79 and 1601, is 126479.

   Considering quadratics of the form:
   n^2 + an + b, where |a| < 1000 and |b| < 1000

   Find the product of the coefficients, a and b, for the quadratic expression
   that produces the maximum number of primes for consecutive values of n,
   starting with n = 0.

   f(n + k) = (n + k)^2 + a(n + k) + b = f(n) + k^2 + ak + 2kn

   Need b prime since f(0) = b, largest value is 997
   We cheat and know n <= 79 since |b| < 1000
   Hence |f(n)| <= |n|^2 + |a||n| + |b| <= 6241 + 79(1000) + 997 = 86238

   Therefore, the biggest we ever have to worry about is 86238 */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

function polynomialConsecutivePrimes(a, b, primes) {
    // f(n + 1) = f(n) + 1 + a + 2n
    var current = b, index = 0;
    while (operator.inArray(current, primes) != -1) {
        current += 1 + a + 2 * index;
        index += 1;
    }
    return index;
};

exports.main = function(verbose) {
    if (typeof verbose == 'undefined') {
        verbose = false;
    }
    var primes = fns.sieve(86238);
    function lessThan1000(prime) {
        return prime < 1000;
    };
    var bChoices = primes.filter(lessThan1000), maxVal = -1,
        maxA, maxB, candidate, a;

    // Algorithm different than python due to memory constraints
    for (var i = 0, b; b = bChoices[i]; i++) {
        for (a = -999; a < 1000; a++) {
            candidate = polynomialConsecutivePrimes(a, b, primes);
            if (candidate > maxVal) {
                maxVal = candidate;
                maxA = a;
                maxB = b;
            }
        }
    }

    if (verbose) {
        return [maxA * maxB, '.\nSetting a = ', maxA, ' and b = ', maxB,
                ' produces ', maxVal, ' consecutive primes.'].join('');
    } else {
        return maxA * maxB;
    }
};

if (require.main === module) {
    timer.timer(27, exports.main);
}
