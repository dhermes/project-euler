// To be used with timer = require('./operator.js')

exports.mul = function(a, b) {
    return Number(a) * Number(b);
};

exports.add = function(a, b) {
    return Number(a) + Number(b);
};

exports.sum = function(arr) {
    return arr.reduce(exports.add, 0);
};

exports.range = function(first, second, third) {
    var interval = 1,
        bottom = 0,
        top;

    if (typeof second == 'undefined') {
        top = first;
    } else {
        bottom = first;
        top = second;
        if (typeof third != 'undefined') {
            interval = third;
        }
    }

    var result = [];
    if (interval > 0) {
        for(var i = bottom; i < top; i += interval) {
            result.push(i);
        }
    } else {
        for(var i = bottom; i > top; i += interval) {
            result.push(i);
        }
    }

    return result;
};
