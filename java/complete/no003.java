class no003 {
// def is_prime(n, primes=[], failure_point=None):
//     if n < 10:
//         return n in [2, 3, 5, 7]

//     # We safely assume n >= 10
//     if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
//         return False

//     if failure_point is not None:
//         if n >= failure_point:
//             raise ValueError("%s is too large for is_prime." % n)

//     if primes != []:
//         if n in primes:
//             return True
//         to_check = [prime for prime in primes if prime**2 <= n]
//         for prime in to_check:
//             if n % prime == 0:
//                 return False
//         return True

//     divisor_bound = int(sqrt(n))
//     # From here, we know only +/- 1 mod 6 works, so
//     # we start with 11 and 13 (primes > 10)
//     divisor_minus, divisor_plus = 11, 13
//     while divisor_minus <= divisor_bound:
//         if n % divisor_minus == 0 or n % divisor_plus == 0:
//             return False
//         divisor_minus += 6
//         divisor_plus += 6
//     return True

// def first_prime_divisor(n, prime_list=[]):
//     if n == 1:
//         return [1, 1]
//     elif n % 2 == 0:
//         return [2, n/2]

//     if prime_list != []:
//         for p in prime_list:
//             if n % p == 0:
//                 return [p, n/p]
//         # To complete this loop, either the prime list was
//         # insufficient or p is prime
//         if is_prime(n, primes=prime_list):
//             return [n, 1]
//         else:
//             raise ValueError("Prime list poorly specified")
//     else:
//         divisor = 3
//         while n % divisor != 0:
//             divisor += 2
//         return [divisor, n/divisor]
//     raise ValueError("Bad input %s." % n)

// def robust_divide(n, quotient, include_count=False):
//     if quotient in (-1, 1):
//         raise ValueError("Please don't use %s as a quotient." % quotient)

//     result = n
//     count = 0
//     while result % quotient == 0:
//         count += 1
//         result = result/quotient
//     if include_count:
//         return result, count
//     else:
//         return result

// def prime_factors(n, unique=False, hash_=None):
//     if n == 1:
//         if type(hash_) == dict:
//             hash_[1] = []
//         return []
//     if type(hash_) == dict and n in hash_:
//         return hash_[n]

//     prime, quotient = first_prime_divisor(n)

//     remaining, count = robust_divide(n, prime, include_count=True)
//     if unique:
//         result = [prime] + prime_factors(remaining,
//                                          unique=unique,
//                                          hash_=hash_)
//     else:
//         result = [prime] * count + prime_factors(remaining,
//                                                  unique=unique,
//                                                  hash_=hash_)

//     if type(hash_) == dict:
//         hash_[n] = result

//     return result

  public static int main(boolean verbose) {
    // return max(prime_factors(600851475143))
    return 1;
  }

  public static int main() {
    return main(false);
  }

  public static void main(String[] args) {
    System.out.println(main());
  }
}
