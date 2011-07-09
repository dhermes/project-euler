/* What is the smallest positive number that is evenly
   divisible by all of the numbers from 1 to 20? */

function gcd(a, b) {
    var M = Math.max(a, b),
        m = Math.min(a, b);
    if (m == 0) {
        return M;
    } else if (M == 0) {
        return m;
    } else if (M == m) {
        return M;
    }
    return gcd(m, M % m);
};

function min_product(n) {
    if (n < 2) {
        return 1;
    }

    var product = min_product(n - 1),
        shared_factors = gcd(product, n);
    return (product*n)/shared_factors;
};

function main() {
    return min_product(20);
};
