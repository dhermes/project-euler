#!/usr/bin/env node

/* What is the first term in the Fibonacci sequence to contain 1000 digits? */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

// from python_code.functions import fibonacci_generator

exports.main = function() {
//     fib = fibonacci_generator()
//     fib_index = 0
//     for value in fib:
//         # number of digits
//         if len(str(value)) < 1000:
//             fib_index += 1
//             continue
//         else:
//             print fib_index
//             break
    return 1;
};

if (require.main === module) {
    timer.timer(25, exports.main);
}
