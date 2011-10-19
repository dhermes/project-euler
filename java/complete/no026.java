import java.util.Arrays;
import java.util.HashMap;

class no026 {
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

  public static long lcm(long n, long m) {
    return (n * m) / gcd(n, m);
  }

  public static long gcd(long a, long b) {
    long M = Math.max(a, b);
    long m = Math.min(a, b);

    if (m == 0) {
      return M;
    } else if (M == 0) {
      return m;
    } else if (M == m) {
      return M;
    }

    return gcd(m, M % m);
  }

  public static long order_mod_n(long value, long n, HashMap<Integer, Integer> hash_, long[] prime_list) throws Exception {
    if (hash_ != null && hash_.containsKey(n)) {
      return hash_.get((int) n);
    }

    if (gcd(value, n) != 1 || n == 1) {
      throw new Exception(value + " is not a unit modulo " + n + ".");
    }

    long[] prime_div_pair = first_prime_divisor(n, prime_list);
    long prime = prime_div_pair[0];
    long quotient = robust_divide(n, prime);

    long base_residue, residue, exponent;
    if (quotient == 1) {
      // at this point, n is not in the hash_ but must be a
      // prime power
      base_residue = value % n;

      residue = base_residue;
      exponent = 1;
      while (residue != 1) {
        residue = (residue * base_residue) % n;
        exponent++;
      }
      hash_.put((int) n, (int) exponent);
      return exponent;
    }

    // Here, quotient > 1
    long prime_power = n / quotient;
    long prime_order = order_mod_n(value, prime_power, hash_, prime_list);
    long quotient_order = order_mod_n(value, quotient, hash_, prime_list);
    hash_.put((int) n, (int) lcm(prime_order, quotient_order));
    return hash_.get((int) n);
  }

  public static long order_mod_n(long value, long n, HashMap<Integer, Integer> hash_) throws Exception {
    return order_mod_n(value, n, hash_, new long[0]);
  }

  public static long order_mod_n(long value, long n, long[] prime_list) throws Exception {
    return order_mod_n(value, n, new HashMap<Integer, Integer>(), prime_list);
  }

  public static long order_mod_n(long value, long n) throws Exception {
    return order_mod_n(value, n, new HashMap<Integer, Integer>(), new long[0]);
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

  public static int main(boolean verbose) {
    int max_index = -1;
    long max_block_size = -1;
    long stripped_val, block_size;
    for (int i = 1; i < 1000; i++) {
      try {
        stripped_val = robust_divide(robust_divide(i, 2), 5);
      } catch (Exception exc) {
        exc.printStackTrace();
        return 0;
      }

      if (stripped_val == 1) {
        block_size = 0;
      } else {
        try {
          block_size = order_mod_n(10, stripped_val);
        } catch (Exception exc) {
          exc.printStackTrace();
          return 111;
        }
      }

      if (block_size > max_block_size) {
        max_block_size = block_size;
        max_index = i;
      }
    }

    return max_index;
  }

  public static int main() {
    return main(false);
  }

  public static void main(String[] args) {
    System.out.println(main(true));
  }
}
