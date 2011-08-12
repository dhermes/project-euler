#!/usr/local/bin/node

/* What is the 10001st prime number? */

var fns = require('../functions.js'),
    timer = require('../timer.js');

function main() {
    /* By the prime number theorem, pi(x) =~ x/ln(x)
       pi(x) >= 10001 when x >= 10001 ln(x)
       To be safe, we'll double it and solve
       x = 20002 ln(x)
       We are left with approximately 248490 */
    var primes = fns.sieve(248490),
        result = primes[10001 - 1];
    return result;
};

timer.timer(7, main);
