#!/usr/bin/env node

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

exports.main = function(verbose) {
    if (typeof verbose == 'undefined') {
        verbose = false;
    }
    var n = 10000,
        factors = fns.allFactors(n - 1);

    // sum of proper divisors
    var firstPass = [], i;
    for (i = 1; i < n; i++) {
        firstPass.push(operator.sum(factors[i]) - 1);
    }
    var maxOut = Math.max.apply(Math, firstPass);

    factors = fns.allFactors(maxOut, factors);
    /* applying sum of divisors twice to i we have
       s_1 = func(i), s_2 = func(s_1)
       s_1 = sum(factors[i]) - i, s_2 = sum(factors[s_1]) - s_1
       i == s_2 <==>
       i == sum(factors[sum(factors[i]) - i]) - (sum(factors[i]) - i) <==>
       sum(factors[sum(factors[i]) - i]) == sum(factors[i])
       Similarly s_1 != i <==> sum(factors[i]) != 2 * i */
    var result = [], factorSum;
    for (i = 2; i < n; i++) {
        factorSum = operator.sum(factors[i]);
        if (factorSum != 2 * i) {
            if (operator.sum(factors[factorSum - i]) == factorSum) {
                result.push(i);
            }
        }
    }

    if (verbose) {
        return [operator.sum(result), '.\nThe full list of such amicable numbers is ',
                result.join(', '), '.'].join('');
    } else {
        return operator.sum(result);
    }
};

if (require.main === module) {
    timer.timer(21, exports.main);
}
