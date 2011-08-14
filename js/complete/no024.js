#!/usr/bin/env node

/* The lexicographic permutations of 0, 1 and 2 are:
          012   021   102   120   201   210
   What is the millionth lexicographic permutation of the
   digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9 */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

function lex(arr, perm) {
    /**
     * Returns the perm-th permutation of the list in order
 
     * The ordering can be thought of like so:
     * Consider the indices representing each step, they will make
     * up all permutations of 0, 1, ..., len(arr) - 1. So we can
     * order them based on the value of this number in base len(arr)
     */
    if (arr.length < 2) {
        return arr.slice();
    }

    var index = Math.floor(perm / fns.factorial(arr.length - 1)),
        remaining = perm % fns.factorial(arr.length - 1),
        arrRemoved = arr.slice(0, index).concat(arr.slice(index + 1));
    return [arr[index]].concat(lex(arrRemoved, remaining));
};

exports.main = function() {
    var arr = operator.range(10),
        // Our indexing begins at 0
        perm = Math.pow(10, 6) - 1;
    return lex(arr, perm).join('');
};

if (require.main === module) {
    timer.timer(24, exports.main);
}
