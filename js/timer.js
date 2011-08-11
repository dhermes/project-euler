// To be used with timer = require('./timer.js')

function timeDiff(time1, time2) {
    var result = 60*(time1.getMinutes() - time2.getMinutes()) +
                 (time1.getSeconds() - time2.getSeconds()) +
                 (time1.getMilliseconds() - time2.getMilliseconds())/1000;
    result = Math.abs(result);
    if (result == 0) {
        return 'less than 0.001 seconds';
    } else if (result == 1) {
        return '1 second';
    } else {
        return result + ' seconds';
    }
};

exports.timer = function (problem_number, main) {
    var timeStart = new Date(),
        result = main(),
        timeEnd = new Date(),
    timeElapsed = timeDiff(timeStart, timeEnd);
    var statement = ['The answer to Euler Project, question ',
                     problem_number, ' is: ',
                     result, '\nThis ran in ', timeElapsed];

    console.log(statement.join(''));
};
