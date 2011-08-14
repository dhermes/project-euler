#!/usr/bin/env node

/* Find the value of d < 1000 for which ^(1)/_(d) contains the
   longest recurring cycle in its decimal fraction part. */

var fns = require('../functions.js'),
    timer = require('../timer.js');

exports.main = function() {
    var maxIndex = -1, maxBlockSize = -1, strippedVal, blockSize;
    for (var i = 1; i < 1000; i++) {
        strippedVal = fns.robustDivide(fns.robustDivide(i, 2), 5);
        if (strippedVal == 1) {
            blockSize = 0;
        } else {
            blockSize = fns.orderModN(10, strippedVal);
        }

        if (blockSize > maxBlockSize) {
            maxBlockSize = blockSize;
            maxIndex = i;
        }
    }
    return maxIndex;
};

if (require.main === module) {
    timer.timer(26, exports.main);
}
