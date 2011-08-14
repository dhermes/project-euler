#!/usr/bin/env node

/* We shall say that an n-digit number is pandigital if it makes use of all
   the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
   and is also prime.

   What is the largest n-digit pandigital prime that exists? */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

// from math import sqrt
// from python_code.functions import all_permutations_digits
// from python_code.functions import is_prime
// from python_code.functions import sieve

exports.main = function() {
//     MAX_n = 987654321
//     PRIMES = sieve(int(sqrt(MAX_n)))
//     for i in range(9, 1, -1):
//         cand = [str(dig) for dig in range(1, i + 1)]
//         cand = int("".join(cand))
//         candidates = sorted(all_permutations_digits(cand))[::-1]
//         for candidate in candidates:
//             if is_prime(candidate, primes=PRIMES, failure_point=MAX_n):
//                 print candidate
//                 return
//     raise ValueError("No prime was found, algorithm busted.")
    return 1;
};

if (require.main === module) {
    timer.timer(41, exports.main);
}
