#!/usr/bin/env node

/* Starting in the top left corner of a 2 x 2 grid, there are
6 routes (without backtracking) to the bottom right corner.
How many routes are there through a 20 x 20 grid? */

var fns = require('../functions.js'),
    timer = require('../timer.js');

exports.main = function() {
    // In an n x m grid there are (n + m) C m = (n + m) C n such paths.
    return fns.choose(20 + 20, 20);
};

if (require.main === module) {
    timer.timer(15, exports.main);
}
