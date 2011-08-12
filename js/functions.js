// To be used with timer = require('./functions.js')

function zero_pad(val, total_length) {
    var result = val.toString();
    while (result.length < total_length) {
	result = "0" + result;
    }
    return result;
};

exports.get_data = function(problem_number) {
    var filename = 'no' + zero_pad(problem_number, 3) + '.txt',
        /* This need to be set differently (currently is based
           on import location */
        path = '../../problem_data/' + filename;

    var fs = require('fs'),
        data = fs.readFileSync(path);
 
    return data.toString('utf8');
};

// Helper for sieve
function filled_array(size, value) {
    var result = [];
    for(var i = 0; i < size; i++) {
        result.push(value);
    }
    return result;
};

exports.sieve = function(n) {
    var to_check = filled_array(n + 1, true);
        result = [];
    for(var i = 2; i <= n; i++) {
        if (to_check[i]) {
            result.push(i);
            for(var j = 2*i; j <= n; j += i) {
                to_check[j] = false;
            }
        }
    }

    return result;
};
