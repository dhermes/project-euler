#!/usr/bin/env node

/* Find the sum of all numbers, less than one million, which
   are palindromic in base 10 and base 2. */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

function binaryIncrementer(str) {
    var digs = str.split('').map(Number), tmp;
    digs[digs.length - 1]++;
    for (var i = digs.length - 1; i >= 0; i--) {
        if (digs[i] > 1) {
            tmp = digs[i];
            digs[i] = tmp % 2;
            if (i) {
                digs[i - 1] += Math.floor(tmp / 2);
            } else {
                digs = [Math.floor(tmp / 2)].concat(digs);
            }
        } else {
            break;
        }
    }
    return digs.join('');
};

function allBase10Base2Palindromes(n) {
    var result = [], base10 = 1, base2 = '1';
    while (base10 < n) {
        if (fns.isPalindrome(base10) && fns.isPalindrome(base2)) {
            result.push(base10);
        }
        base10++;
        base2 = binaryIncrementer(base2);
    }
    return result;
};

exports.main = function(verbose) {
    if (typeof verbose == 'undefined') {
        verbose = false;
    }

    var ans = allBase10Base2Palindromes(Math.pow(10, 6));
    if (verbose) {
        return [operator.sum(ans), '.\nThe full list of palindromes is: ',
                ans.join(', '), '.'].join('');
    } else {
        return operator.sum(ans);
    }
};

if (require.main === module) {
    timer.timer(36, exports.main);
}
