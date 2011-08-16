#!/usr/bin/env node

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

exports.main = function(verbose) {
    if (typeof verbose == 'undefined') {
        verbose = false;
    }
    var n = 100, powers = fns.applyToList(operator.bigIntPow, operator.range(2, n + 1));
    powers = operator.uniqSorted(powers, false);
    return powers.length;
};

if (require.main === module) {
    timer.timer(29, exports.main);
}
