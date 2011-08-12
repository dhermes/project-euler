// To be used with timer = require('./operator.js')

exports.mul = function(a, b) {
    return Number(a)*Number(b);
};

exports.add = function(a, b) {
    return Number(a) + Number(b);
};

exports.sum = function(arr) {
    return arr.reduce(exports.add, 0);
};
