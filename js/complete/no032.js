#!/usr/bin/env node

/* an n-digit number is >= 10^(n-1)
   n*m >= 10^(n+m-2), must have at least n + m - 1  digits

   subsets of cardinality 5,6 */

var operator = require('../operator.js'),
    timer = require('../timer.js');

function allOrderings(arr) {
    if (arr.length == 1) {
        return [arr];
    }

    var result = [], sublist;
    for (var i = 0; i < arr.length; i++) {
        sublist = arr.slice(0, i).concat(arr.slice(i + 1));
        function addEltMap(ordering) {
            return ordering.concat(arr[i]);
        };
        result = result.concat(allOrderings(sublist).map(addEltMap));
    }
    return result;
};

/* Will take a list and break it at various places, returning
   the product of the integers formed */
function possibleProducts(arr) {
    var result = [], left, right;
    for (var i = 1; i < arr.length; i++) { 
        left = arr.slice(0, i).join('');
        right = arr.slice(i).join('');
        result.push(Number(left) * Number(right));
    }

    return result;
};

exports.main = function() {
    var products = [], candidates = allOrderings(operator.range(1, 10)), prods, last4, last3;
    for (var i = 0, candidate; candidate = candidates[i]; i++) {
        prods = possibleProducts(candidate.slice(0, 5));
        last4 = Number(candidate.slice(-4).join(''));
        if (operator.inArray(last4, prods) != -1 && operator.inArray(last4, products) == -1) {
            products.push(last4);
        }

        prods = possibleProducts(candidates.slice(0, 6));
        last3 = Number(candidate.slice(-3).join(''));
        if (operator.inArray(last3, prods) != -1 && operator.inArray(last3, products) == -1) {
            products.push(last3);
        }
    }

    return operator.sum(products);
};

if (require.main === module) {
    timer.timer(32, exports.main);
}
