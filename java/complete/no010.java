import java.util.Arrays;

class no010 {
  public static int [] sieve(int n) {
    boolean[] to_check = new boolean[n + 1];
    Arrays.fill(to_check, true);
    int final_check = (int) Math.sqrt(n);

    for (int i = 2; i <= final_check; i++) {
      if (to_check[i]) {
        for (int j = i * i; j <= n; j += i) {
          to_check[j] = false;
        }
      }
    }

    int[] result = new int[n];
    int curr_index = 0;
    for (int i = 2; i <= n; i++) {
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

  public static long main(boolean verbose) {
    int[] primes = sieve(2000000 - 1);

    long result = 0;
    for (int i = 0; i < primes.length; i++) {
      result += primes[i];
    }

    return result;
  }

  public static long main() {
    return main(false);
  }

  public static void main(String[] args) {
    System.out.println(main(true));
  }
}
