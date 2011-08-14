#!/usr/bin/env node

/* The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
   increases by 3330, is unusual in two ways: (i) each of the three
   terms are prime, and, (ii) each of the 4-digit numbers are
   permutations of one another.

   There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
   primes, exhibiting this property, but there is one other 4-digit
   increasing sequence.

   What 12-digit number do you form by concatenating the three terms
   in this sequence? */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

// from python_code.functions import all_subsets
// from python_code.functions import sieve

// def find_arithmetic(list_):
//     if len(list_) < 3:
//         raise ValueError("List wrong size.")

//     candidates = all_subsets(list_, 3)
//     for cand in candidates:
//         if cand[0] + cand[2] == 2*cand[1]:
//             return cand
//     return []

exports.main = function() {
//     primes = [prime for prime in sieve(10000) if prime > 999]
//     primes_by_digits = {}
//     for prime in primes:
//         key = "".join(sorted([digit for digit in str(prime)]))
//         if key in primes_by_digits:
//             primes_by_digits[key].append(prime)
//         else:
//             primes_by_digits[key] = [prime]

//     result = []
//     for key in primes_by_digits:
//         candidate = primes_by_digits[key]
//         if len(candidate) >= 3:
//             soln = find_arithmetic(candidate)
//             if soln:
//                 result.append("".join([str(num) for num in soln]))
//     print result[0]
    return 1;
};

if (require.main === module) {
    timer.timer(49, exports.main);
}
