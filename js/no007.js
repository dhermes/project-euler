/* What is the 10001st prime number? */

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

function main() {
    /* By the prime number theorem, pi(x) =~ x/ln(x)
       pi(x) >= 10001 when x >= 10001 ln(x)
       To be safe, we'll double it and solve
       x = 20002 ln(x)
       We are left with approximately 248490 */
    var primes = sieve(248490),
        result = primes[10001-1];
    return result;
};
