#!/usr/bin/env node

/* What is the largest 1 to 9 pandigital 9-digit number that can be formed as
   the concatenated product of an integer with (1,2, ... , n) where n > 1? */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

// def is_pandigital_9(str_):
//     for dig in [str(elt) for elt in range(1, 10)]:
//         if str_.count(dig) != 1:
//             return False
//     return True

// def all_pandigitals_1_to_n(n):
//     to_mult = range(1, n + 1)
//     multiplier = 1
//     result = []

//     curr = "".join([str(multiplier*elt) for elt in to_mult])
//     while len(curr) < 10:
//         if is_pandigital_9(curr):
//             result.append(curr)
//         multiplier += 1
//         curr = "".join([str(multiplier*elt) for elt in to_mult])

//     return result

exports.main = function() {
//     result = []
//     for n in range(2, 10):
//         result.extend(all_pandigitals_1_to_n(n))
//     print max([int(elt) for elt in result])
    return 1;
};

if (require.main === module) {
    timer.timer(38, exports.main);
}
