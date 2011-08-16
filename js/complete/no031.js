#!/usr/bin/env node

/* In England there are 8 coins in circulation:
   1p, 2p, 5p, 10p, 20p, 50p, 100p and 200p.
   How many different ways can 200p be made using any number of coins?

   This will be the coeficient of x^200 in
   (1 + x + x^2 + ...)(1 + x^2 + x^4 + ...)(1 + x^5 + x^10 + ...)*...
   ...*(1 + x^10 + x^20 + ...)(1 + x^20 + x^40 + ...)(1 + x^50 + x^100 + ...) */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

function polynomialAdd(left, right) {
    var maxLen = Math.max(left.length, right.length),
        toAddLeft = fns.filledArray(maxLen - left.length, 0).concat(left),
        toAddRight = fns.filledArray(maxLen - right.length, 0).concat(right);
    function toAddMap(index) {
        return toAddLeft[index] + toAddRight[index];
    };
    return operator.range(maxLen).map(toAddMap);
};

/* represent ax^n + bx^(n-1) + ... + c as [c,...b,a]
   1 + 2x + x^2 + 2x^3 = (1+2x)*(1+x^2) =
   [1,2]*[1,0,1] = [1,0,1,0] + [2,0,2] = [1,2,1,2] */
function polynomialMult(f, g) {
    var result = [], toAdd;
    for (var ind = 0; ind < f.length; ind++) {
        function multEltMap(coeff) {
            return f[f.length - ind - 1] * coeff;
        };
        toAdd = g.map(multEltMap).concat(fns.filledArray(ind, 0));
        result = polynomialAdd(result, toAdd);
    }
    return result;
};

function generatingPoly(maxPower, base) {
    var addOn = fns.filledArray(base - 1, 0).concat(1),
        result = [1];
    for (var i = 0; i < Math.floor(maxPower /  base); i++) {
        result = result.concat(addOn);
    }
    return result;
};

exports.main = function(verbose) {
    if (typeof verbose == 'undefined') {
        verbose = false;
    }
    var prod = generatingPoly(200, 1),
        coins = [2, 5, 10, 20, 50, 100, 200];
    for (var i = 0, coin; coin = coins[i]; i++) {
        prod = polynomialMult(prod, generatingPoly(200, coin));
    }
    return prod[200];
};

if (require.main === module) {
    timer.timer(31, exports.main);
}
