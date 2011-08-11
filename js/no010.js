/* Find the sum of all the primes below two million. */

function filled_array(size, value) {
    var result = [];
    for(var i = 0; i < size; i++) {
        result.push(value);
    }
    return result;
};

function sieve(n) {
    var to_check = filled_array(n+1, true);
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

function sum(arr) {
    //not robust, expects integers or strings
    result = 0;
    for(var i = 0, val; val = arr[i]; i++) {
        result += val;
    }
    return result;
};

function main() {
    var primes = sieve(2000000),
        result = sum(primes);
    return result;
};

timer = require('./timer.js');
timer.timer(10, main);
