#!/usr/bin/env node

/* Find the last ten digits of the series 1^1 + 2^2 + 3^3 + ... + 1000^1000. */

var bigint = require('bigint'),
    timer = require('../timer.js');

exports.main = function() {
    var result = bigint(0), modulus = Math.pow(10, 10);
    for (var i = 1; i <= 1000; i++) {
	result = result.add(bigint(i).powm(i, modulus)).mod(modulus);
    }
    return result.toString();
};

if (require.main === module) {
    timer.timer(48, exports.main);
}
