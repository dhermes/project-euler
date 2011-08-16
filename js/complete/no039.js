#!/usr/bin/env node

/* For p, we seek k, m, n > 0 such that n < m and 2*k*m*(m + n) = p */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

function allTriples(p, factorsHash) {
    if (typeof factorsHash == 'undefined') {
        factorsHash = {};
    }

    if (p % 2 || p < 2) {
        return [];
    }

    var choicesK;
    // We know p % 2 == 0
    if (p / 2 in factorsHash) {
        choicesK = factorsHash[p / 2];
    } else {
        choicesK = fns.allFactors(p / 2, factorsHash)[p / 2];
    }

    var result = [], choicesM, j, m, n;
    for (var i = 0, k; k = choicesK[i]; i++) {
        if (p / (2 * k) in factorsHash) {
            choicesM = factorsHash[p / (2 * k)];
        } else {
            choicesM = fns.allFactors(p / (2 * k), factorsHash)[p / (2 * k)];
        }

        // 2 * k * m * (m + n) == p
        for (j = 0; m = choicesM[j]; j++) {
            n = p / (2 * k * m) - m;
            if (n > 0 && m > n) {
                result.push([k, m, n]);
            }
        }
    }

    return result;
};

function convertToTriangle(triple) {
    var k = triple[0], m = triple[1], n = triple[2],
        a = k * (m * m - n * n),
        b = k * (2 * m * n),
        c = k * (m * m + n * n);
    return operator.uniqSorted([a, b, c]);
};

function allTriangles(p, factorsHash) {
    if (typeof factorsHash == 'undefined') {
        factorsHash = {};
    }

    var triples = allTriples(p, factorsHash);
    function stringMap(triangle) {
        return triangle.join(', ');
    };

    function undoStringMap(str) {
        return str.split(', ').map(Number);
    };
    return operator.uniqSorted(triples.map(convertToTriangle).map(stringMap), false).map(undoStringMap);
};

function allTrianglesUpToN(n) {
    var factorsHash = fns.allFactors(n), result = {};
    for (var p = 2; p <= n; p += 2) {
        result[p] = allTriangles(p, factorsHash);
    }
    return result;
};

exports.main = function(verbose) {
    if (typeof verbose == 'undefined') {
        verbose = false;
    }
    var allTri = allTrianglesUpToN(1000), lengths = {}, maxVal = -1, maxKeys = [], key;
    for (key in allTri) {
        currLength = allTri[key].length;
        if (currLength > maxVal) {
            maxKeys = [key];
            maxVal = currLength;
        } else if (currLength == maxVal) {
            maxKeys.push(key);
        }
    }

    if (maxKeys.length != 1) {
        return; // Keys are not unique
    }
    return maxKeys[0];
};

if (require.main === module) {
    timer.timer(39, exports.main);
}
