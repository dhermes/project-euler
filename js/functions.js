// To be used with timer = require('./functions.js')

var bigint = require('bigint'),
    operator = require('./operator.js');

////////////////////////////////////////////////////////////
///////////////////// HELPER FUNCTIONS /////////////////////
////////////////////////////////////////////////////////////

// Helper for sieve
function filledArray(size, value) {
    // Returns [value, value, ..., value] (of size size)
    var result = [];
    for (var i = 0; i < size; i++) {
        result.push(value);
    }
    return result;
};

exports.zeroPad = function(val, totalLength) {
    var result = val.toString();
    while (result.length < totalLength) {
	result = '0' + result;
    }
    return result;
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

exports.lcm = function(n, m) {
    return n * m / exports.gcd(n, m);
};

// Substitute since math (python) library DNE
exports.factorial = function(n, useBigint) {
    if (typeof useBigint == 'undefined') {
        useBigint = false;
    }

    if (n == 0 || n == 1) {
        return useBigint ? '1' : 1;
    } else {
        if (useBigint) {
            return bigint(exports.factorial(n - 1, useBigint)).mul(n).toString();
        } else {
            return n * exports.factorial(n - 1, useBigint);
        }
    }
};

exports.choose = function(n, k) {
    var fact = exports.factorial;
    return fact(n) / (fact(k) * fact(n - k));
};

exports.getData = function(problemNumber) {
    var filename = 'no' + exports.zeroPad(problemNumber, 3) + '.txt',
        /* This need to be set differently (currently is based
           on import location */
        path = '../../problem_data/' + filename;

    var fs = require('fs'),
        data = fs.readFileSync(path);
 
    return data.toString('utf8');
};

function robustDivide(n, quotient, includeCount) {
    if (typeof includeCount == 'undefined') {
        includeCount = false;
    }

    if (quotient == 1 || quotient == -1) {
        return;
    }

    var result = n,
        count = 0;

    while (result % quotient == 0) {
        count += 1;
        result = result / quotient;
    }

    if (includeCount) {
        return [result, count];
    } else {
        return result;
    }
};

exports.recurrenceNext = function(relation, values) {
    /* Assumes recurrence of length k satisfies
    f(n + k) = relation[0] * f(n) + relation[1] * f(n + 1) + ...

    Values are also expected to be ordered [f(n), f(n + 1),...] */
    if (relation.length == values.length) {
        var nextVal = 0;
        for (var i = 0; i < relation.length; i++) {
            nextVal += relation[i] * values[i];
        }

        // copies values (doesn't change inputs)
        var result = values.slice(1).concat(nextVal);
        return result;
    }
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

exports.isPower = function(n, exponent) {
    var floorVal = Math.floor(Math.pow(n, 1 / exponent));
    return (n == Math.pow(floorVal, exponent));
};

////////////////////////////////////////////////////////////
///////////////////// PROBLEM SPECIFIC /////////////////////
////////////////////////////////////////////////////////////

exports.maxSum = function(triangleMatrix) {
    /**
     * Finds maximum sum of path from top of triangle down to bottom
     * 
     * Input: Matrix of triangle e.g.
     * 1
     * 3 5
     * 7 8 4
     * becomes [[1], [3, 5], [7, 8, 4]]
     * Uses memoization from the bottom layer up to work quickly
     * Output: maximum value
     */
    var maxDepth = triangleMatrix.length - 1;

    // Set bottom row for memoization
    var depth = maxDepth, result = {};
    for (var i = 0, entry; entry = triangleMatrix[depth][i]; i++) {
        result[i + ',' + (maxDepth - depth)] = entry;
    }
    depth -= 1;

    /* Set each row moving up the triangle based on
       the results one low below */
    var valLeft, valRight;
    while (depth >= 0) {
        for (var i = 0, entry; entry = triangleMatrix[depth][i]; i++) {
            valLeft = result[i + ',' + (maxDepth - depth - 1)];
            valRight = result[(i + 1) + ',' + (maxDepth - depth - 1)];
            result[i + ',' + (maxDepth - depth)] = entry + Math.max(valLeft, valRight);
        }
        depth -= 1;
    }

    return result[0 + ',' + (maxDepth - depth - 1)];
};

exports.fillCount = function(m, n) {
    var count = 1, maxK = Math.floor((n + 1)/(m + 1));

    var sumAI, permCount, addValue, bottom, asc, gpAI, i;
    for (var k = 1; k <= maxK; k++) {
        for (sumAI = m * k; sumAI <= n + 1 - k; sumAI++) {
            permCount = 0;
            for (bottom = m; bottom < Math.floor(sumAI / k) + 1; bottom++) {
                asc = exports.ascending(k, sumAI, bottom, n + 1);
                for (i = 0; gpAI = asc[i]; i++) {
                    permCount += exports.totalPerms(gpAI);
                }
            }
            addValue = permCount * (exports.choose(n + 1 - sumAI, k));
            count += addValue;
        }
    }

    return count;
};

exports.primeDividesRepunitPower10 = function(prime, cap) {
    /* Determines if a prime divides any repunit R(10^n)
       if cap > 0, then we set a max on the value of n */
    if (typeof cap == 'undefined') {
        cap = -1;
    }

    if (operator.inArray(prime, [2, 3, 5]) != -1) {
        return false;
    }
    var countTwo = robustDivide(prime - 1, 2, true),
        countFive = robustDivide(prime - 1, 5, true);
    countTwo = countTwo[1];
    countFive = countFive[1];

    if (cap > 0) {
        countTwo = Math.min(cap, countTwo);
        countFive = Math.min(cap, countFive);
    }

    if (prime == Math.pow(2, countTwo) * Math.pow(5, countFive) + 1) {
        return true;
    }

    var expTwo, expFive, possibleExp = [];
    for (expTwo = 0; expTwo <= countTwo; expTwo++) {
        for (expFive = 0; expFive <= countFive; expFive++) {
            possibleExp.push(Math.pow(2, expTwo) * Math.pow(5, expFive));
        }
    }
    possibleExp.sort(operator.sortNumber);

    for (var i = 0, exp ; exp = possibleExp[i]; i++) {
        if ((Math.pow(10, exp) - 1) % prime == 0) {
            return true;
        }
    }
    return false;
};

////////////////////////////////////////////////////////////
////////////////////////// PRIMES //////////////////////////
////////////////////////////////////////////////////////////

function firstPrimeDivisor(n, primeList) {
    if (typeof primeList == 'undefined') {
        primeList = [];
    }

    if (n === 1) {
        return [1, 1];
    } else if (n % 2 == 0) {
        return [2, n / 2];
    }

    if (primeList.length) {
        for (var i = 0, p; p = primeList[i]; i++) {
            if (n % p == 0) {
                return [p, n / p];
            }
        }
        /* To complete this loop, either the prime list was
           insufficient or p is prime */
        
        if (exports.isPrime(n, primeList)) {
            return [n, 1];
        } else {
            return; // Prime list poorly specified
        }
    } else {
        var divisor = 3;
        while (n % divisor != 0) {
            divisor += 2;
        }

        return [divisor, n / divisor];
    }
};

exports.primeFactors = function(n, unique, hash) {
    if (typeof unique == 'undefined') {
        unique = false;
    }

    if (typeof hash == 'undefined') {
        hash = {};
    }

    if (n === 1) {
        hash[1] = [];
        return [];
    } else if (n in hash) {
        return hash[n];
    }

    var divisionPair = firstPrimeDivisor(n),
        prime = divisionPair[0],
        quotient = divisionPair[1],
        robustPair = robustDivide(n, prime, true),
        remaining = robustPair[0],
        count = robustPair[1];

    var result;
    if (unique) {
        result = [prime].concat(exports.primeFactors(remaining, unique, hash));
    } else {
        result = filledArray(count, prime).concat(exports.primeFactors(remaining, unique, hash));
    }

    hash[n] = result;
    return result;
};

exports.factors = function(n, factorHash, primes) {
    if (typeof factorHash == 'undefined') {
        factorHash = {};
    }
    if (typeof primes == 'undefined') {
        primes = [];
    }

    if (n in factorHash) {
        return factorHash[n];
    } else if (n == 1) {
        factorHash[1] = [1];
        return [1];
    } else if (operator.inArray(n, primes) != -1) {
        factorHash[n] = [1, n];
        return [1, n];
    }
    
    var divis = firstPrimeDivisor(n, primes),
        prime = divis[0],
        quotient = divis[1],
        // Need a deep-ish copy
        toAdd = exports.factors(quotient, factorHash, primes).slice();
    function multMap(factor) {
        return prime * factor;
    };
    toAdd = toAdd.concat(toAdd.map(multMap));

    factorHash[n] = operator.uniqSorted(toAdd);
    return factorHash[n];
};

exports.allFactors = function(n, hash) {
    /**
     * Takes n and optional hash of factors
     *
     * Uses the hash to update a full list of factors for
     * all integers 1 to n. Only updates if not in hash
     */
    if (typeof hash == 'undefined') {
        hash = {1: [1], 2: [1, 2], 3: [1, 3]};
    }

    var factorHash = operator.extend({}, hash);
    if (n in factorHash) {
        return factorHash;
    }

    var allPrimes = exports.sieve(n), reduced;

    for (var i = 4; i <= n; i++) {
        if (!(i in factorHash)) {
            reduced = firstPrimeDivisor(i, allPrimes);
            // This will update factor hash
            exports.factors(i, factorHash, allPrimes);
        }
    }

    return factorHash;
};

exports.isPrime = function(n, primes, failurePoint) {
    if (n < 10) {
        return (operator.inArray(n, [2, 3, 5, 7]) != -1);
    }

    // We safely assume n >= 10
    if (n % 2 == 0 || n % 3 == 0 || n % 5 == 0 || n % 7 == 0) {
        return false;
    }

    if (typeof failurePoint != 'undefined' && n >= failurePoint) {
        return; // n is too large for isPrime
    }

    if (typeof primes != 'undefined' && primes.length) {
        if (operator.inArray(n, primes) != -1) {
            return true;
        }

        for (var i = 0, prime; prime = primes[i], prime * prime < n; i++) {
            if (n % prime == 0) {
                return false;
            }
        }
        return true;
    }

    var divisorBound = Math.floor(Math.sqrt(n)),
        /* From here, we know only +/- 1 mod 6 works, so
           we start with 11 and 13 (primes > 10) */
        divisorMinus = 11, divisorPlus = 13;
    while (divisorMinus <= divisorBound) {
        if (n % divisorMinus == 0 || n % divisorPlus == 0) {
            return false;
        }
        divisorMinus += 6;
        divisorPlus += 6;
    }
    return true;
};

exports.sieve = function(n) {
    /**
     * Sieve of Eratosthenes
     *
     * Returns all primes <= n
    */
    var toCheck = filledArray(n + 1, true);
        result = [];
    for (var i = 2; i <= n; i++) {
        if (toCheck[i]) {
            result.push(i);
            for (var j = 2 * i; j <= n; j += i) {
                toCheck[j] = false;
            }
        }
    }

    return result;
};

////////////////////////////////////////////////////////////
///////////////// NUMBER THEORY AND ALGEBRA ////////////////
////////////////////////////////////////////////////////////

exports.orderModN = function(value, n, hash, primeList) {
    if (typeof hash == 'undefined') {
        hash = {};
    }
    if (typeof primeList == 'undefined') {
        primeList = [];
    }

    if (n in hash) {
        return hash[n];
    }

    if (exports.gcd(value, n) != 1 || n == 1) {
        return; // value is not a unit modulo n.
    }

    var divis = firstPrimeDivisor(n, primeList),
        prime = divis[0],
        quotient = robustDivide(n, prime);
    if (quotient == 1) {
        /* at this point, n is not in the hash_ but must be a
           prime power */
        var baseResidue = value % n;
        if (baseResidue < 0) {
            baseResidue += n;
        }

        var residue = baseResidue, exponent = 1;
        while (residue != 1) {
            residue = (residue * baseResidue) % n;
            exponent++;
        }
        hash[n] = exponent;
        return exponent;
    }

    // Here, quotient > 1
    var primePower = n / quotient,
        primeOrder = exports.orderModN(value, primePower, hash, primeList),
        quotientOrder = exports.orderModN(value, quotient, hash, primeList);

    hash[n] = exports.lcm(primeOrder, quotientOrder);
    return hash[n];
};

exports.polynomialRoots = function(coefficients) {
    /* Assumes coefficients = [a_0, a_1,..., a_n]
       for f(x) = a_n x^n + ... + a_1 x + a_0 */
    if (coefficients.length != 3) {
        return; // Only supporting quadratics at this time
    }
    var c = coefficients[0], b = coefficients[1], a = coefficients[2],
        discriminantSqrt = Math.sqrt(Math.pow(b, 2) - 4 * a * c);
    return [(-b + discriminantSqrt) / (2 * a), (-b - discriminantSqrt) / (2 * a)];
};

exports.polygonalNumber = function(s, n) {
    return n * ((s - 2) * n - (s - 4)) / 2;
}

exports.reversePolygonalNumber = function(sides, number, hash) {
    /**
     * Returns n given that number is the nth polygonal
     * number with respect to sides
     *
     * The n-th polygonal number for s sides is:
     * n * ((s - 2) * n - (s - 4)) / 2
     */
    if (typeof hash == 'undefined') {
        hash = {};
    }

    if (number in hash) {
        return hash[number];
    }

    var roots = polynomial_roots([-2 * number, 4 - sides, sides - 2]),
        rootPlus = roots[0], result;
    if (rootPlus != Math.floor(rootPlus)) {
        result = -1;
    } else {
        result = rootPlus;
    }

    hash[number] = result;
    return result;
};

exports.mu = function(n, hash, primes) {
    if (n in hash) {
        return hash[n];
    }

    var divis = firstPrimeDivisor(n, primes),
        prime = divis[0],
    if (n % Math.pow(prime, 2) == 0) {
        hash[n] = 0;
    } else {
        /* if n/prime has a square, we will want mu(n) = 0
           if mu(n/prime) = 1, we add 1 prime so we negate it
           similarly if mu(n/prime) = -1 */
        hash[n] = -exports.mu(n / prime, hash, primes);
    }
    return hash[n];
};

exports.extendedEuclid = function(a, b) {
    var M = Math.max(a, b),
        m = Math.min(a, b),
        last = [M, [1, 0]],
        curr = [m, [0, 1]];

    // Assumes a and b are coprime (terminates at 1
    var next, factor, tmp;
    while (curr[0] > 1) {
        next = last[0] % curr[0];
        factor = (last[0] - next) / curr[0];

        tmp = [next, [last[1][0] - factor * curr[1][0], 
                      last[1][1] - factor * curr[1][1]]];
        last = curr;
        curr = tmp;
    }
    var result = curr[1];

    if (a * result[0] + b * result[1] == 1) {
        return result;
    } else {
        return result.reverse();
    }
};

exports.inverseModN = function(val, n) {
    if (exports.gcd(val, n) > 1) {
        return; // Not invertible
    }

    var result = extendedEuclid(val, n);
    return result[0] % n;
};

////////////////////////////////////////////////////////////
////////////////////// LIST MANAGEMENT /////////////////////
////////////////////////////////////////////////////////////

exports.applyToList = function(fn, arr, nonMatch) {
    if (typeof nonMatch == 'undefined') {
        nonMatch = false;
    }
    var result = [];
    for (var i = 0, val1; val1 = arr[i]; i++) {
        for (var j = 0, val2; val2 = arr[j]; j++) {
            if ((nonMatch && val1 != val2) || !nonMatch) {
                result.push(fn(val1, val2));
            }
        }
    }

    return result;
};

////////////////////////////////////////////////////////////
//////////////////////// GRAPH THEORY //////////////////////
////////////////////////////////////////////////////////////

exports.totalPerms = function(oList) {
    // Input is assumed to be ordered list
    var counts = [], currEntry = oList[0], currCount = 1;
    
    for (var i = 1, entry; entry = oList[i]; i++) {
        if (entry == currEntry) {
            currCount++;
        } else {
            counts.push(currCount);
            currEntry = entry;
            currCount = 1;
        }
    }
    counts.push(currCount);

    var denominator = counts.map(exports.factorial).reduce(operator.mul, 1);
    return exports.factorial(operator.sum(counts)) / denominator;
};

exports.ascending = function(num, numSum, minNum, probMax) {
    if (numSum < minNum) {
        return [];
    }

    if (numSum == 1) {
        if (numSum == minNum) {
            return [[numSum]];
        } else {
            return [];
        }
    }

    var nextSum = numSum - minNum,
        biggest = Math.min(Math.floor(nextSum / (num - 1)), probMax),
       result = [], asc;

    for (var nextMin = minNum; nextMin <= biggest; nextMin++) {
        asc = exports.ascending(num - 1, nextSum, nextMin, probMax);
        function candidateMap(candidate) {
            return [minNum].concat(candidate);
        }
        result = result.concat(asc.map(candidateMap));
    }

    return result;
};
