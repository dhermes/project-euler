#!/usr/bin/env node

var fns = require('./functions.js'),
    fs = require('fs'),
    operator = require('./operator.js'),
    path, stats, main, timeStart, result, timeEnd, timeTotal;

var argv = require('optimist')
    .usage('Usage: $0 [--sum] [--iterations <num>] [--fast]')
    .boolean('sum')
    .boolean('fast')
    .default('sum', false)
    .default('iterations', 1)
    .default('fast', false)
    .argv;

var problemList;
if (argv.fast) {
    problemList = [1, 2, 3, 5, 6, 8, 13, 15, 16, 18, 19, 20, 24, 28, 40, 45];
} else {
    problemList = operator.range(1, 50 + 1);
}

var j;
for (var i = 0, problemNumber; problemNumber = problemList[i]; i++) {
    path = './complete/no' + fns.zeroPad(problemNumber, 3) + '.js';
    try {
        stats = fs.statSync(path);
    } catch (e) {
        path = './too_slow/no' + fns.zeroPad(problemNumber, 3) + '.js';
    }    

    main = require(path);

    timeStart = new Date();
    for (j = 0; j < argv.iterations; j++) {
        result = main.main();
    }
    timeEnd = new Date();
    // Time in milliseconds
    timeTotal = timeEnd - timeStart;

    if (!argv.sum) {
        timeTotal = Math.floor(timeTotal / argv.iterations);
    }

    console.log(problemNumber + ': ' + result + ', ' + timeTotal + 'ms');
}
