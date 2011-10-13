// To be used with timer = require('./timer.js')

function timeDiff(time1, time2) {
  // Assumes times are instantiated via new Date()
  var result = Math.abs(time1 - time2)/1000;
  if (result == 0) {
    return 'less than 0.001 seconds';
  } else if (result == 1) {
    return '1 second';
  } else {
    return result + ' seconds';
  }
};

exports.timer = function (problemNumber, main) {
  var timeStart = new Date(),
      result = main(true),
      timeEnd = new Date(),
  timeElapsed = timeDiff(timeStart, timeEnd);
  var statement = ['The answer to Euler Project, question ',
                   problemNumber, ' is: ',
                   result, '\n\nThis solution ran in ', timeElapsed];

  console.log(statement.join(''));
};
