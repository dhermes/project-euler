import java.util.Arrays;

class no027 {
  public static int [] sieve(int n) {
    boolean[] to_check = new boolean[n + 1];
    Arrays.fill(to_check, true);
    int final_check = (int) Math.sqrt(n);

    for (int i = 2; i < final_check + 1; i++) {
      if (to_check[i]) {
        for (int j = i * i; j < n + 1; j += i) {
          to_check[j] = false;
        }
      }
    }

    int[] result = new int[n];
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

  public static int polynomial_consecutive_primes(int a, int b, int[] primes) {
    // f(n + 1) = f(n) + 1 + a + 2n
    int current = b;
    int index = 0;

    // primes must be sorted
    int found_index = Arrays.binarySearch(primes, current);
    while (found_index >= 0) {
      current += 1 + a + 2 * index;
      index++;

      found_index = Arrays.binarySearch(primes, current);
    }
    return index;
  }

  public static String main(boolean verbose) {
    int[] PRIMES = sieve(86238); // this is sorted
    int biggest_under_1000 = 999;
    int index = Arrays.binarySearch(PRIMES, biggest_under_1000);
    while (index < 0) {
      biggest_under_1000--;
      index = Arrays.binarySearch(PRIMES, biggest_under_1000);
    }
    int[] b_choices = Arrays.copyOfRange(PRIMES, 0, index + 1);

    //    int[][] candidates = new int[(2000 - 1) * b_choices.length];
    int a_at_max = -1;
    int b_at_max = -1;
    int max_vals = 0;
    int curr_val, b;
    for (int a = -999; a < 1000; a++) {
      for (int b_index = 0; b_index < b_choices.length; b_index++) {
        b = b_choices[b_index];
        curr_val = polynomial_consecutive_primes(a, b, PRIMES);
        if (curr_val > max_vals) {
          max_vals = curr_val;
          a_at_max = a;
          b_at_max = b;
        }
      }
    }
    int prod = a_at_max * b_at_max;

    String result = Integer.toString(prod);
    if (verbose) {
      result += ".\nSetting a = " + a_at_max;
      result += " and b = " + b_at_max + " produces ";
      result += max_vals + " consecutive primes.";
    }
    return result;
  }

  public static String main() {
    return main(false);
  }

  public static void main(String[] args) {
    System.out.println(main(true));
  }
}
