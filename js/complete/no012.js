#!/usr/bin/env node

/* What is the value of the first triangle number to have over
five hundred divisors? */

var fns = require('../functions.js'),
    timer = require('../timer.js');

function listFrequencies(arr) {
    var result = {};
    for(var i = 0, element; element = arr[i]; i++) {
        if (element in result) {
            result[element]++;
        } else {
            result[element] = 1;
        }
    }

    return result;
};

function specialNumFactors(a, b, hash) {
    var factors = fns.primeFactors(a, false, hash), product = 1;
    factors = factors.concat(fns.primeFactors(b, false, hash));
    factors = listFrequencies(factors);

    var key;
    for (key in factors) {
        product *= factors[key] + 1;
    }

    return product;
};

function numFactorsNthTriangular(n, hash) {
    if (n % 2) {
        return specialNumFactors(n, (n + 1) / 2, hash);
    } else {
        return specialNumFactors(n / 2, n + 1, hash);
    }
};

function main() {
    var n = 1, h = {},
        numFac = numFactorsNthTriangular(n, h);

    while (numFac <= 500) {
        n += 1;
        numFac = numFactorsNthTriangular(n, h);
    }

    var result = [n * (n + 1) / 2, '.\nIt is the ', n, 'th triangular number and has ',
                  numFac, ' divisors.'].join('');
    return result;
};

timer.timer(12, main);
