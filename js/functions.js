// To be used with timer = require('./functions.js')

function zeroPad(val, totalLength) {
    var result = val.toString();
    while (result.length < totalLength) {
	result = "0" + result;
    }
    return result;
};

exports.getData = function(problemNumber) {
    var filename = 'no' + zeroPad(problemNumber, 3) + '.txt',
        /* This need to be set differently (currently is based
           on import location */
        path = '../../problem_data/' + filename;

    var fs = require('fs'),
        data = fs.readFileSync(path);
 
    return data.toString('utf8');
};

// Helper for sieve
function filledArray(size, value) {
    var result = [];
    for(var i = 0; i < size; i++) {
        result.push(value);
    }
    return result;
};

exports.sieve = function(n) {
    var toCheck = filledArray(n + 1, true);
        result = [];
    for(var i = 2; i <= n; i++) {
        if (toCheck[i]) {
            result.push(i);
            for(var j = 2 * i; j <= n; j += i) {
                toCheck[j] = false;
            }
        }
    }

    return result;
};

exports.recurrenceNext = function(relation, values) {
    /* Assumes recurrence of length k satisfies
    f(n + k) = relation[0] * f(n) + relation[1] * f(n + 1) + ...

    Values are also expected to be ordered [f(n), f(n + 1),...] */
    if (relation.length == values.length) {
        var nextVal = 0;
        for(var i = 0; i < relation.length; i++) {
            nextVal += relation[i] * values[i];
        }

        var result = values.slice(1).concat(nextVal);
        return result;
    }
};

function firstPrimeDivisor(n) {
    if (n === 1) {
        return [1, 1];
    }

    var divisor = 2;
    while (n % divisor != 0) {
        divisor += 1;
    }
    return [divisor, n / divisor];
};

exports.primeFactors = function(n) {
    if (n === 1) {
        return [];
    }

    var division = firstPrimeDivisor(n);
    var prime = division[0];
    var quotient = division[1];

    var remaining = quotient;
    while (remaining % prime == 0) {
        remaining = remaining / prime;
    }

    return [prime].concat(exports.primeFactors(remaining));
};

exports.applyToList = function(fn, arr, nonMatch) {
    if (typeof nonMatch == 'undefined') {
        nonMatch = false;
    }
    var result = [];
    for(var i = 0, val1; val1 = arr[i]; i++) {
        for(var j = 0, val2; val2 = arr[j]; j++) {
            if ((nonMatch && val1 != val2) || !nonMatch) {
                result.push(fn(val1, val2));
            }
        }
    }

    return result;
};

exports.isPalindrome = function(n) {
    var n = n.toString();
    if (n.length < 2) {
        return true;
    } else if (n[0] != n[n.length - 1]) {
        return false;
    }
    return exports.isPalindrome(n.slice(1, n.length - 1));
};

exports.gcd = function(a, b) {
    var M = Math.max(a, b),
        m = Math.min(a, b);
    if (m == 0) {
        return M;
    } else if (M == 0) {
        return m;
    } else if (M == m) {
        return M;
    }

    return exports.gcd(m, M % m);
};

exports.polygonalNumber = function(s, n) {
    return n * ((s - 2) * n - (s - 4)) / 2;
}
