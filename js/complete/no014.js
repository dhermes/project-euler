#!/usr/bin/env node

/* Which starting number, under one million, produces the
longest chain? (Of the collatz chain) */

var timer = require('../timer.js');

function collatzNext(n) {
    if (n % 2) {
        return 3 * n + 1;
    } else {
        return n / 2;
    }
};

function length(n, hash) {
    if (n in hash) {
        return hash[n];
    } else {
        var currLength = 1 + length(collatzNext(n), hash);
        hash[n] = currLength;
        return currLength;
    }
};

function maxCollatzLengthUpToN(n, hash) {
    if (typeof hash == 'undefined') {
        hash = {1: 1};
    }

    var maxLength = -1, maxLengthAt = -1, currLength;
    for (var i = 1; i <= n; i++) {
        currLength = length(i, hash);
        if (currLength > maxLength) {
            maxLength = currLength;
            maxLengthAt = i;
        }
    }

    return [maxLengthAt, maxLength];
};

exports.main = function() {
    var ans = maxCollatzLengthUpToN(999999);
    return [ans[0], '.\nThe Collatz chain at ', ans[0],
            ' has length ', ans[1], '.'].join('');
};

if (require.main === module) {
    timer.timer(14, exports.main);
}
