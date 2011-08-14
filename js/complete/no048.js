#!/usr/bin/env node

/* Find the last ten digits of the series 1^1 + 2^2 + 3^3 + ... + 1000^1000. */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

exports.main = function() {
//     result = 0
//     for i in range(1, 1000 + 1):
//         result = (result + pow(i, i, 10**10)) % 10**10
//     print result
    return 1;
};

if (require.main === module) {
    timer.timer(48, exports.main);
}
