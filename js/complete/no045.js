#!/usr/bin/env node

/* Triangular: T_n = n(n+1)/2
   Pentagonal: P_n = n(3n-1)/2
   Hexagonal: H_n = n(2n-1)

   T_285 = P_165 = H_143
   Find the next such Triangular number.

   T and H: a^2 + a = 4c^2 - 2c
   4a^2 + 4a + 1 = 16c^2 - 8c + 1
   (2a + 1)^2 = (4c - 1)^2
   2a + 1 = 4c - 1
   a = 2c - 1

   T and P: a^2 + a = 3b^2 - b
   4a^2 + 4a + 1 = 12b^2 - 4b + 1
   3(2a + 1)^2 = 36b^2 - 12b + 1 + 2 = (6b - 1)^2 + 2
   Solve 3x^2 - y^2 = 2
   Required: x = 2a + 1 = 4c - 1, y = 6b - 1 (modular residues)

   Base solution (x,y) = (1,1), if we view the river of the form
   f((x,y)) = 3x^2 - y^2 with u_0 = (1,0) and v_0 = (0,1) we have
   f(u_0) = 3, f(v_0) = -1 we have the general transformation along the 
   river u_{n+1} = 2u_n + 3v_n, v_{n+1} = u_n + 2v_n
   which gives u_{n+2} - 2u_{n+1} - 2(u_{n+1} - 2u_n) 
   = 3v_{n+1} - 2(3v_n) = 3u_n which implies
   u_{n+2} - 4u_{n+1} + u_n = 0 (and similarly for v_n)
   We know also that since u + v gives the solutions to 3x^2 - y^2 = 2
   that the solutions we want also follow this recurrence. 
   Let s_0 = (1,1) and s_1 = (3,5)
   We seek solutions s_n such that s_n(x) = 3 mod 4 and s_n(y) = 5 mod 6.

   s_n(x) Modulo 4:
   f{n+2} = 4f{n+1} - f{n} = -f{n} mod 4
   1, 3, 3, 1, 1, 3, 3, 1, 1, 3, 3, ...
   indices == 1 and 2 mod 4 give s_n(x) == 3

   s_n(y) Modulo 6:
   f{n+2} = 4f{n+1} - f{n}
   (1, 5,) (1, 5,) (1, 5,) (1, 5,) (1, 5,) ...
   indices == 1 mod 2

   Combining we must have n == 1 mod 4

   The solution we were given is a = 285, x = 2a + 1 = 571 which gives y = 989
   and is at index 5

   The next solution happens when n = 9
   2a + 1 = x_9
   8T_a + 1 = 4a^2 + 4a + 1 =  x_9^2
   T_a = (x_9^2 - 1)/8 */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

exports.main = function() {
//     a, b = 1, 3
//     for i in range(8):
//         a, b = b, 4*b - a
//     # Now b = x_9
//     print (b**2 - 1)/8
    return 1;
};

if (require.main === module) {
    timer.timer(45, exports.main);
}
