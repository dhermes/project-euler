import java.util.Arrays;
import java.util.HashMap;

class no023 {
  public static long [] sieve(long n) {
    boolean[] to_check = new boolean[(int) n + 1];
    Arrays.fill(to_check, true);
    long final_check = (long) Math.sqrt(n);

    for (int i = 2; i < final_check + 1; i++) {
      if (to_check[i]) {
        for (int j = i * i; j < n + 1; j += i) {
          to_check[j] = false;
        }
      }
    }

    long[] result = new long[(int) n];
    int curr_index = 0;
    for (int i = 2; i < n + 1; i++) {
      if (to_check[i]) {
        result[curr_index] = i;
        curr_index++;
      }
    }

    if (curr_index != n) {
      result = Arrays.copyOfRange(result, 0, curr_index);
    }
    return result;
  }

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

  public static long[] factors(long n, HashMap<Long, long[]> factor_hash, long[] primes) throws Exception {
    if (factor_hash != null && factor_hash.containsKey(n)) {
      return factor_hash.get(n);
    } else if (n == 1) {
      factor_hash.put((long) 1, new long[] {1});
      return factor_hash.get((long) 1);
    }

    Arrays.sort(primes);
    long index = Arrays.binarySearch(primes, n);
    if (index != -1) {
      factor_hash.put(n, new long[] {1, n});
      factor_hash.get(n);
    }

    long[] prime_quotient = first_prime_divisor(n, primes);
    long prime = prime_quotient[0];
    long quotient = prime_quotient[1];

    long[] to_mult = factors(quotient, factor_hash, primes);
    int length = to_mult.length;
    to_mult = Arrays.copyOf(to_mult, length * 2);
    for (int i = 0; i < length; i++) {
      to_mult[i + length] = prime * to_mult[i];
    }
    Arrays.sort(to_mult);

    long[] to_add = new long[to_mult.length];
    to_add[0] = to_mult[0];
    int curr_index = 1;

    long prev = to_mult[0];
    long curr = to_mult[0];
    for (int i = 1; i < to_mult.length; i++) {
      prev = curr;
      curr = to_mult[i];
      if (curr > prev) {
        to_add[curr_index] = curr;
        curr_index++;
      }
    }
    to_add = Arrays.copyOfRange(to_add, 0, curr_index);
    factor_hash.put(n, to_add);

    return factor_hash.get(n);
  }

  public static long[] factors(long n, HashMap<Long, long[]> factor_hash) throws Exception {
    return factors(n, factor_hash, new long[0]);
  }

  public static long[] factors(long n, long[] primes) throws Exception {
    return factors(n, new HashMap<Long, long[]>(), primes);
  }

  public static long[] factors(long n) throws Exception {
    return factors(n, new HashMap<Long, long[]>(), new long[0]);
  }

  public static HashMap<Long, long[]> all_factors(long n, HashMap<Long, long[]> hash_)  throws Exception {
    HashMap<Long, long[]> factor_hash = (HashMap<Long, long[]>) hash_.clone();
    if (factor_hash != null && factor_hash.containsKey(n)) {
      return factor_hash;
    }

    long[] all_primes = sieve(n);
    long[] reduced;
    for (int i = 4; i < n + 1; i++) {
      if (factor_hash != null && factor_hash.containsKey(i)) {
         continue;
      }
      reduced = first_prime_divisor(i, all_primes);
      // This will update factor hash
      factors(i, factor_hash, all_primes);
    }

    return factor_hash;
  }

  public static HashMap<Long, long[]> all_factors(long n) throws Exception {
    HashMap<Long, long[]> hash_ = new HashMap<Long, long[]>();
    hash_.put((long) 1, new long[] {1});
    hash_.put((long) 2, new long[] {1, 2});
    hash_.put((long) 3, new long[] {1, 3});
    return all_factors(n, hash_);
  }

  public static String join(String join_val, String[] arr) {
    String result = "";
    int length = arr.length;
    for (int i = 0; i < length - 1; i++) {
      result += arr[i] + join_val;
    }

    if (length > 0) {
      result += arr[length - 1];
    }

    return result;
  }

  public static String join(String join_val, long[] arr) {
    String result = "";
    int length = arr.length;
    for (int i = 0; i < length - 1; i++) {
      result += Long.toString(arr[i]) + join_val;
    }

    if (length > 0) {
      result += Long.toString(arr[length - 1]);
    }

    return result;
  }

  public static long array_sum(long[] arr) {
    if (arr == null || arr.length == 0) {
      return 0;
    } else {
      long result = 0;
      for (int i = 0; i < arr.length; i++) {
        result += arr[i];
      }
      return result;
    }
  }

  public static int array_sum(int[] arr) {
    if (arr == null || arr.length == 0) {
      return 0;
    } else {
      int result = 0;
      for (int i = 0; i < arr.length; i++) {
        result += arr[i];
      }
      return result;
    }
  }

  public static int[] abundant_numbers(int n) throws Exception {
    HashMap<Long, long[]> factor_hash = all_factors((long) n);
    // sum of proper divisors
    int[] result = new int[n - 1];
    int curr_index = 0;
    for (int i = 2; i < n + 1; i++) {
      if (i < array_sum(factor_hash.get((long) i)) - i) {
        result[curr_index] = i;
        curr_index++;
      }
    }
    result = Arrays.copyOfRange(result, 0, curr_index);
    return result;
  }

  public static int main(boolean verbose) {
    int[] abundants = new int[0];
    try {
      abundants = abundant_numbers(28123);
    } catch (Exception exc) {
      exc.printStackTrace();
    }
    boolean[] sums = new boolean[28123 + 1]; // Filled with false by default

    int length = abundants.length;
    int val1, val2;
    for (int index = 0; index < length; index++) {
      for (int second_index = index; second_index < length; second_index++) {
        val1 = abundants[index];
        val2 = abundants[second_index];
        if (val1 + val2 <= 28123) {
          sums[val1 + val2] = true;
        }
      }
    }

    int result = 0;
    for (int i = 0; i < sums.length; i++) {
      if (!sums[i]) {
        result += i;
      }
    }
    return result;
  }

  public static int main() {
    return main(false);
  }

  public static void main(String[] args) {
    System.out.println(main(true));
  }
}
