#!/usr/bin/env node

/* Work out the first ten digits of the sum of the following
one-hundred 50-digit numbers. (In data) */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

exports.main = function() {
    function nonEmptyFilter(str) {
        return (str != '');
    };
    var numbers = fns.getData(13).split('\n').filter(nonEmptyFilter),
        total = operator.bigintSum(numbers);
    return String(total).slice(0, 10);
};

if (require.main === module) {
    timer.timer(13, exports.main);
}
