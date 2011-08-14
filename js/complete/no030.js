#!/usr/bin/env node

/* Find the sum of all the numbers that can be written
   as the sum of fifth powers of their digits.

   n = d-digits, sum(n) <= d*9^5 = 59049d, n >= 10^(d-1),
   so sum(n) = n implies 10*(9**5 d) >= 10**d,
   ln(10 * 9**5) + ln(d) >= d ln(10), so d <= 6 */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

// def sum_of_digits_powers(n, power):
//     return sum([int(dig)**power for dig in str(n)])

exports.main = function() {
//     valid = []
//     for i in xrange(2,999999 + 1):
//         if sum_of_digits_powers(i, 5) == i:
//             valid.append(i)

//     print "%s.\nThe numbers satisfying this property are: %s." % (sum(valid),
//         ", ".join([str(num) for num in valid]))
    return 1;
};

if (require.main === module) {
    timer.timer(30, exports.main);
}
