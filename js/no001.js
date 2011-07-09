/* If we list all the natural numbers below 10 that are multiples of 3 or 5,
   we get 3, 5, 6 and 9. The sum of these multiples is 23.
  
   Find the sum of all the multiples of 3 or 5 below 1000. */
function all_multiples(bound, base) {
    var result = [];
    for(var i = 0; base*(i + 1) < bound; i++) {
        result[i] = base*(i + 1);
    }
    return result;
};

function unique(arr) {
    var hash = {}
    for(var i = 0, val; val = arr[i]; i++) {
        if (hash.hasOwnProperty(val)) {
            hash[val] += 1;
        } else {
            hash[val] = 1;
        }
    }

    var result = [];
    for(var key in hash) {
        result.push(parseInt(key));
    }
    return result;
};

function sum(arr) {
    //not robust, expects integers or strings
    var result = 0;
    for(var i = 0, val; val = arr[i]; i++) {
        result += val;
    }
    return result;
};

function main() {
    var both_sets = all_multiples(1000, 3).concat(all_multiples(1000, 5)),
        uniq_mults = unique(both_sets),
        final = sum(uniq_mults);

    return final;
};
