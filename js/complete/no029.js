#!/usr/bin/env node

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

// from python_code.functions import apply_to_list

exports.main = function() {
//     n = 100
//     powers = apply_to_list(operator.pow, range(2, n + 1))
//     print len(set(powers))
    return 1;
};

if (require.main === module) {
    timer.timer(29, exports.main);
}
