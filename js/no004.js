/* A palindromic number reads the same both ways. The largest
   palindrome made from the product of two 2-digit numbers is
   9009 = 91 * 99.

   Find the largest palindrome made from the product of two
   3-digit numbers. */

function is_palindrome(n) {
    var str_n = n.toString();
    if (str_n.length < 2) {
        return true;
    }
    if (str_n[0] != str_n[str_n.length-1]) {
        return false;
    }
    return is_palindrome(str_n.slice(1,str_n.length-1));
};

function products(arr) {
    var result = [];
    for(var i = 0, val1; val1 = arr[i]; i++) {
        for(var j = 0, val2; val2 = arr[j]; j++) {
            result.push(val1*val2);
        }
    }
    return result;
};

function main() {
    var three_digits = [];
    for (var num = 100; num < 1000; num++){
        three_digits.push(num);
    }
    var all_products = products(three_digits);
    var result = -1;
    for(var i = 0, prod; prod = all_products[i]; i++) {
        if (is_palindrome(prod)) {
            if (prod > result) {
                result = prod;
            }
        }
    }

    return result;
};
