// To be used with timer = require('./operator.js')

var bigint = require('bigint');

exports.mul = function(a, b) {
    return Number(a) * Number(b);
};

exports.add = function(a, b) {
    return Number(a) + Number(b);
};

exports.sum = function(arr) {
    return arr.reduce(exports.add, 0);
};

exports.bigintSum = function(arr) {
    // assumes arr is full of strings
    var result = bigint('0');
    for (var i = 0, curr; curr = arr[i]; i++) {
        result = result.add(curr);
    }
    return result.toString();
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

exports.inArray = function(val, arr) {
    for (var i = 0, curr; curr = arr[i]; i++) {
        if (curr == val) {
            return i;
        }
    }

    return -1;
};

exports.sortNumber = function(a, b) {
    return a - b;
};

exports.uniqSorted = function(arr) {
    var result = [];
    for (var i = 0, val; val = arr[i]; i++) {
        if (exports.inArray(val, result) == -1) {
            result.push(val);
        }
    }
    result.sort(exports.sortNumber);
    return result;
};

exports.extend = function(destination, source) {
    for (var property in source) {
        if (source.hasOwnProperty(property)) {
            destination[property] = source[property];
        }
    }
    return destination;
};
