#!/usr/bin/env node

/* The lexicographic permutations of 0, 1 and 2 are:
          012   021   102   120   201   210
   What is the millionth lexicographic permutation of the
   digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9 */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

// from math import factorial

// def lex(list_, perm):
//     """
//     Returns the perm-th permutation of the list in order

//     The ordering can be thought of like so:
//     Consider the indices representing each step, they will make
//     up all permutations of 0, 1, ..., len(list_) - 1. So we can
//     order them based on the value of this number in base len(list_)
//     """
//     if len(list_) < 2:
//         return list_[:]

//     index = perm/factorial(len(list_) - 1) # int. division intended
//     remaining = perm % factorial(len(list_) - 1)
//     return [list_[index]] + lex(list_[:index]+list_[index+1:], remaining)

exports.main = function() {
//     list_ = range(10)
//     perm = 10**6 - 1 # Our indexing begins at 0
//     print "".join([str(dig) for dig in lex(list_, perm)])
    return 1;
};

if (require.main === module) {
    timer.timer(24, exports.main);
}
