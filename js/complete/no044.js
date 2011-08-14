#!/usr/bin/env node

/* Pentagonal is n(3n-1)/2
   Find (j,k) for which P_j + P_k and abs(P_j - P_k) = D is pentagonal and D is minimized. What is D?

   We will infinitely generate (k,j) = (1,2), (1,3), (2,3), (1,4), (2,4), ...
   We will infinitely generate (k,j) = (1,2), (2,3), (1,3), (3,4), (2,4), (1,4), (4,5), ...
   Will check if P_j - P_k is pentagonal.
   If it is, will then check if P_k + P_j is

   NOTE: P_j - P_k is increasing in j and decreasing in k, so if we fix j, it is
   minimized when k is largest, i.e. P_j - P_(j - 1)
   = (3j**2 - j)/2 - (3(j - 1)**2 - (j - 1))/2 = 3j - 2

   For k < j, P_j - P_k >= 3j - 2
   So if we have established a difference D, if 3j - 2 >= D, we need not consider it,
   hence we need k < j < (D + 2)/3 */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

function incrementPair(pair) {
    /**
     * Increments pair by traversing through all
     * k for a given j until 1 is reached, then starting
     * back up with the next highest value for j
     *
     * E.G. [1,2]-->[2,3]-->[1,3]-->[3,4]-->[2,4]-->...
     */
    var k = pair[0], j = pair[1];
    k--;
    if (k > 0) {
        return [k, j];
    } else {
        return [j, j + 1];
    }
};

exports.main = function() {
    /* Not only finds the minimum, but also checks to make sure
       it is the smallest. Since P_j - P_k >= P_j - P_(j-1) = 3j - 2
       If 3j - 2 > D, then P_j - P_k > D, and we not longer need to
       check the minimum */
    var pair = [1, 2], D = -1, vals, difference, last;
    while (D == -1 || 3 * pair[1] - 2 <= D) {
        vals = [fns.polygonalNumber(5, pair[0]), fns.polygonalNumber(5, pair[1])];
        difference = Math.abs(vals[0] - vals[1]);
        if (D != -1 && difference > D) {
            /* since increment decreases the first argument, if
               we go past the difference, we can stop checking
               [k, j] for a fixed j, and we just bypass
               by incrementing j */
            last = pair[1];
            pair = [last, last + 1];
        } else {
            if (fns.reversePolygonalNumber(5, difference) != -1) {
                if (fns.reversePolygonalNumber(5, operator.sum(vals)) != -1) {
                    if (D == -1 || difference < D) {
                        D = difference;
                    }
                }
            }
            pair = incrementPair(pair);
        }
    }
    return D;
};

if (require.main === module) {
    timer.timer(44, exports.main);
}
