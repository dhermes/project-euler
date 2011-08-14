#!/usr/bin/env node

/* Using no022.txt, a text file containing over five-thousand first names,
   begin by sorting it into alphabetical order. Then working out the
   alphabetical value for each name, multiply this value by its alphabetical
   position in the list to obtain a name score.

   For example, when the list is sorted into alphabetical order, COLIN,
   which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
   So, COLIN would obtain a score of 938 X 53 = 49714.

   What is the total of all the name scores in the file? */

var fns = require('../functions.js'),
    timer = require('../timer.js');

function nameScore(name) {
    name = name.toUpperCase();
    var baseVal = 'A'.charCodeAt(0) - 1, result = 0;
    for (var i = 0; i < name.length; i++) {
        result += name.charCodeAt(i) - baseVal;
    }
    return result;
};

exports.main = function() {
    // The name file is a comma separated file with quotes
    var names = fns.getData(22).slice(1, -1).split('","'), result = 0;
    names.sort();
    for (var i = 0, name; name = names[i]; i++) {
        result += (i + 1) * nameScore(name);
    }
    return result;
};

if (require.main === module) {
    timer.timer(22, exports.main);
}
