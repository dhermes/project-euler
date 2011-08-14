#!/usr/bin/env node

/* an n-digit number is >= 10^(n-1)
   n*m >= 10^(n+m-2), must have at least n + m - 1  digits

   subsets of cardinality 5,6 */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

// def all_orderings(list_):
//     if len(list_) == 1:
//         return [list_]

//     result = []
//     for elt in list_:
//         sublist = list_[:]
//         sublist.remove(elt)
//         result.extend([[elt] + ordering
//                        for ordering in all_orderings(sublist)])

//     return result

// # Will take a list and break it at various places, returning
// # the product of the integers formed
// def possible_products(list_):
//     result = []

//     for i in range(1,len(list_)):
//         left = list_[:i]
//         left = int("".join([str(elt) for elt in left]))
//         right = list_[i:]
//         right = int("".join([str(elt) for elt in right]))
//         result.append(left*right)

//     return result

exports.main = function() {
//     products = set()
//     candidates = all_orderings(range(1,10))
//     for candidate in candidates:
//         prods = possible_products(candidate[:5])
//         last4 = candidate[-4:]
//         last4 = int("".join([str(elt) for elt in last4]))
//         if last4 in prods:
//             products.add(last4)

//         prods = possible_products(candidate[:6])
//         last3 = candidate[-3:]
//         last3 = int("".join([str(elt) for elt in last3]))
//         if last3 in prods:
//             products.add(last3)

//     print sum(products)
    return 1;
};

if (require.main === module) {
    timer.timer(32, exports.main);
}
