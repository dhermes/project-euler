import java.util.Arrays;

class no007 {
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

  public static int main(boolean verbose) {
    int [] primes = sieve(248490);
    return primes[10001 - 1];
  }

  public static int main() {
    return main(false);
  }

  public static void main(String[] args) {
    System.out.println(main(true));
  }
}
