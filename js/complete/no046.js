#!/usr/bin/env node

/* What is the smallest odd composite n that can't be written n = p + 2k^2
   for some prime p and some integer k? */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

// from python_code.functions import is_power
// from python_code.functions import sieve

// def is_possible(n, primes):
//     if n % 2 == 0 or n in primes:
//         raise Error("Value poorly specified")

//     primes_less = [prime for prime in primes if prime < n and prime != 2]
//     for prime in primes_less:
//         if is_power((n - prime)/2.0, 2):
//             return True
//     return False

exports.main = function() {
//     # sieve(6000) will do it (answer is 5777)
//     curr = 9
//     primes = sieve(5777)
//     while is_possible(curr, primes):
//         curr += 2
//         while curr in primes:
//             curr += 2
//     print curr
    return 1;
};

if (require.main === module) {
    timer.timer(46, exports.main);
}
