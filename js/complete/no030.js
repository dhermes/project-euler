#!/usr/bin/env node

/* Find the sum of all the numbers that can be written
   as the sum of fifth powers of their digits.

   n = d-digits, sum(n) <= d*9^5 = 59049d, n >= 10^(d-1),
   so sum(n) = n implies 10*(9**5 d) >= 10**d,
   ln(10 * 9**5) + ln(d) >= d ln(10), so d <= 6 */

var operator = require('../operator.js'),
    timer = require('../timer.js');

function sumOfDigitsPowers(n, power) {
    function mapPower(dig) {
        return Math.pow(Number(dig), power);
    };
    return operator.sum(n.toString().split('').map(mapPower));
};

exports.main = function() {
    var valid = [];
    for (var i = 2; i < 1000000; i++) {
        if (sumOfDigitsPowers(i, 5) == i) {
            valid.push(i);
        }
    }

    return [operator.sum(valid), '.\nThe numbers satisfying this property are: ',
            valid.join(', '), '.'].join('');
};

if (require.main === module) {
    timer.timer(30, exports.main);
}
