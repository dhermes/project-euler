#!/usr/bin/env node

/* Find the value of d < 1000 for which ^(1)/_(d) contains the
   longest recurring cycle in its decimal fraction part. */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

// from python_code.functions import order_mod_n
// from python_code.functions import robust_divide

exports.main = function() {
//     max_index = -1
//     max_block_size = -1
//     for i in range(1, 1000):
//         stripped_val = robust_divide(robust_divide(i, 2), 5)
//         if stripped_val == 1:
//             block_size = 0
//         else:
//             block_size = order_mod_n(10, stripped_val)
//         if block_size > max_block_size:
//             max_block_size = block_size
//             max_index = i
//     print max_index
    return 1;
};

if (require.main === module) {
    timer.timer(26, exports.main);
}
