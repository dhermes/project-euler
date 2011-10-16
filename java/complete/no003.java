import java.util.Arrays;
import java.util.HashMap;

class no003 {
  public static boolean is_prime(long n, long[] primes, long failure_point) throws Exception {
    if (n < 10) {
      return (n == 2 || n == 3 || n == 5 || n == 7);
    }

    // We safely assume n >= 10
    if (n % 2 == 0 || n % 3 == 0 || n % 5 == 0 || n % 7 == 0) {
      return false;
    }

    if (failure_point != -1 && n >= failure_point) {
      throw new Exception(n + " is too large for is_prime.");
    }

    if (primes != null && primes.length != 0) {
      Arrays.sort(primes);
      long found_index = Arrays.binarySearch(primes, n);
      if (found_index >= 0) {
        return true;
      }

      int curr_index = 0;
      long prime = primes[curr_index];
      while (prime * prime <= n && curr_index < primes.length) {
        if (n % prime == 0) {
          return false;
        }
      }

      return true;
    }

    long divisor_bound = (long) Math.sqrt(n);
    // From here, we know only +/- 1 mod 6 works, so
    // we start with 11 and 13 (primes > 10)
    long divisor_minus = 11;
    long divisor_plus = 13;
    while (divisor_minus <= divisor_bound) {
      if (n % divisor_minus == 0 || n % divisor_plus == 0) {
        return false;
      }
      divisor_minus += 6;
      divisor_plus += 6;
    }
    return true;
  }

  public static boolean is_prime(long n, long[] primes) throws Exception {
    return is_prime(n, primes, -1);
  }

  public static boolean is_prime(long n, long failure_point) throws Exception {
    return is_prime(n, new long[0], failure_point);
  }

  public static boolean is_prime(long n) throws Exception {
    return is_prime(n, new long[0], -1);
  }

  public static long[] first_prime_divisor(long n, long[] prime_list) throws Exception {
    if (n == 1) {
      return new long[] {1, 1};
    } else if (n % 2 == 0) {
      return new long[] {2, n / 2};
    }

    if (prime_list != null && prime_list.length != 0) {
      long p;
      for (int i = 0; i < prime_list.length; i++) {
        p = prime_list[i];
        if (n % p == 0) {
          return new long[] {p, n / p};
        }
      }

      // To complete this loop, either the prime list was
      // insufficient or p is prime
      if (is_prime(n, prime_list)) {
        return new long[] {n, 1};
      } else {
        throw new Exception("Prime list poorly specified");
      }
    } else {
      long divisor = 3;
      while (n % divisor != 0) {
        divisor += 2;
      }
      return new long[] {divisor, n / divisor};
    }
  }

  public static long[] first_prime_divisor(long n) throws Exception {
    return first_prime_divisor(n, new long[0]);
  }

  public static long[] robust_divide(long n, long quotient, boolean include_count) throws Exception {
    if (quotient == 1 || quotient == -1) {
      throw new Exception("Please don't use " + quotient + " as a quotient.");
    }
    
    // Since method can only return one type, we assume include_count is
    // always true, and throw an error otherwise
    if (!include_count) {
      throw new Exception("include_count shall always be true.");
    }

    long result = n;
    long count = 0;
    while (result % quotient == 0) {
      count++;
      result = result / quotient;
    }

    return new long[] {result, count};
  }

  public static long robust_divide(long n, long quotient) throws Exception {
    long[] result = robust_divide(n, quotient, true);
    return result[0];
  }

  public static long[] prime_factors(long n, boolean unique, HashMap<String, long []> hash_) throws Exception {
    if (n == 1) {
      if (hash_ != null) {
        hash_.put(Long.toString(n), new long[0]);
      }
    return new long[0];
    }

    if (hash_ != null && hash_.containsKey(Long.toString(n))) {
      return hash_.get(Long.toString(n));
    }

    long[] to_map = first_prime_divisor(n); // Worry about n
    long prime = to_map[0];
    long quotient = to_map[1];

    to_map = robust_divide(n, prime, true);
    long remaining = to_map[0];
    int count = (int) to_map[1];

    long[] tmp = prime_factors(remaining, unique, hash_);
    long[] result;
    if (unique) {
      result = new long[1 + tmp.length];

      result[0] = prime;

      for (int i = 0; i < tmp.length; i++) {
        result[i + 1] = tmp[i];
      }
    } else {
      result = new long[count + tmp.length];

      for (int i = 0; i < count; i++) {
        result[i] = prime;
      }

      for (int i = 0; i < tmp.length; i++) {
        result[i + count] = tmp[i];
      }
    }

    if (hash_ != null) {
      return hash_.put(Long.toString(n), result);
    }

    return result;
  }

  public static long[] prime_factors(long n, boolean unique) throws Exception {
    return prime_factors(n, unique, null);
  }

  public static long[] prime_factors(long n, HashMap<String, long []> hash_) throws Exception {
    return prime_factors(n, false, hash_);
  }

  public static long[] prime_factors(long n) throws Exception {
    return prime_factors(n, false, null);
  }

  public static long main(boolean verbose) {
    try {
      long[] factors = prime_factors(600851475143L);
      Arrays.sort(factors);
      return factors[factors.length - 1];
    } catch (Exception exc) {
      exc.printStackTrace();
      return 0;
    }
  }

  public static long main() {
    return main(false);
  }

  public static void main(String[] args) {
    System.out.println(main());
  }
}
