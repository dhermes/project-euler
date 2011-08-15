var fns = require('./functions.js'),
    fs = require('fs'), 
    path, stats, main, timeStart, result, timeEnd;

for (var problemNumber = 1; problemNumber <= 50; problemNumber++) {
    path = './complete/no' + fns.zeroPad(problemNumber, 3) + '.js';
    try {
        stats = fs.statSync(path);
    } catch (e) {
        path = './too_slow/no' + fns.zeroPad(problemNumber, 3) + '.js';
    }    

    main = require(path);
    timeStart = new Date();
    result = main.main();
    timeEnd = new Date();
    // Time in milliseconds
    console.log(problemNumber + ': ' + result + ', ' + Math.abs(timeStart - timeEnd) + 'ms');
}
