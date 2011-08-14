#!/usr/bin/env node

/* The number, 197, is called a circular prime because all
   rotations of the digits: 197, 971, and 719, are themselves prime.

   How many circular primes are there below one million? */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

function containsOnlyDigits(n, digits) {
    var nDigits = n.toString().split('').map(Number);
    for (var i = 0, dig; dig = nDigits[i]; i++) {
        if (operator.inArray(dig, digits) == -1) {
            return false;
        }
    }
    return true;
};

function allCircularPerms(arr) {
    var n = arr.length, result = [], indices;

    function modularIndexLookupMap(index) {
        return arr[index % n];
    };

    for (var lead = 0; lead < n; lead++) {
        result.push(operator.range(lead, lead + n).map(modularIndexLookupMap));
    }
    return result;
};

function allCircularPermsInt(n) {
    var digs = n.toString().split('');
    function permJoinMap(perm) {
        return Number(perm.join(''));
    };
    return allCircularPerms(digs).map(permJoinMap);
};

function allCircularPermIn(prime, primes) {
    var perms = allCircularPermsInt(prime);
    for (var i = 0, perm; perm = perms[i]; i++) {
        if (operator.inArray(perm, primes) == -1) {
            return false;
        }
    }
    return true;
};

function allCircular(n) {
    // the number of digits limits the size of all permutations
    var digs = n.toString().length;
    function sieveFilter(prime) {
        return containsOnlyDigits(prime, [1, 3, 7, 9]);
    };
    var possiblePrimes = fns.sieve(Math.pow(10, digs) - 1).filter(sieveFilter).concat([2, 5]);

    function possiblePrimesFilter(prime) {
        return (prime <= n && allCircularPermIn(prime, possiblePrimes));
    };
    return possiblePrimes.filter(possiblePrimesFilter);
};

exports.main = function() {
    var result = allCircular(Math.pow(10, 6) - 1);
    return result.length;
};

if (require.main === module) {
    timer.timer(35, exports.main);
}
