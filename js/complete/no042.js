#!/usr/bin/env node

/* By converting each letter in a word to a number corresponding to
   its alphabetical position and adding these values we form a word
   value. For example, the word value for SKY is
   19 + 11 + 25 = 55 = t_(10). If the word value is a triangle number
   then we shall call the word a triangle word.

   Using words.txt (right click and 'Save Link/Target As...'), a 16K
   text file containing nearly two-thousand common English words,
   how many are triangle words?

   I've renamed words.txt as no042.txt */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

function wordToValue(word) {
    var letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    function indexToVal(letter) {
        return operator.inArray(letter, letters) + 1;
    };
    return operator.sum(word.split('').map(indexToVal));
};

function numTriangle() {
    // Assumes file is "A","ABILITIY","ABLE",...
    var words = fns.getData(42).slice(1, -1).split('","'),
        vals = words.map(wordToValue),
        triangleHash = {}, count = 0;
    for (var i = 0, val; val = vals[i]; i++) {
        if (fns.reversePolygonalNumber(3, val, triangleHash) != -1) {
            count++;
        }
    }
    return count;
};

exports.main = function(verbose) {
    if (typeof verbose == 'undefined') {
        verbose = false;
    }
    return numTriangle();
};

if (require.main === module) {
    timer.timer(42, exports.main);
}
