#!/usr/bin/env node

/* Find the sum of all numbers which are equal to the sum
   of the factorial of their digits.

   We know if n has d digits, then sum(n) <= d*9! = 362880d and n >= 10*(d-1)
   hence sum(n) = n implies 3628800d >= 10^d. We must have d <= 7. */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

// from math import factorial

// def fact_sum_digs(n):
//     return sum([factorial(int(dig)) for dig in str(n)])

exports.main = function() {
//     result = []
//     for i in xrange(3, 9999999 + 1):
//         if fact_sum_digs(i) == i:
//             result.append(i)
//     print "%s.\nThe full list of numbers is as follows: %s." % (sum(result),
//         ", ".join([str(number) for number in result]))
    return 1;
};

if (require.main === module) {
    timer.timer(34, exports.main);
}
