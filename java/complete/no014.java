import java.util.Arrays;
import java.util.HashMap;

class no014 {
  public static long collatz_next(long n) {
    if (n % 2 == 0) {
      return n / 2;
    } else {
      return 3 * n + 1;
    }
  }

  public static long length(long n, HashMap<Long, Long> hash_) {
    if (hash_ != null && hash_.containsKey(n)) {
      return hash_.get(n);
    } else {
      Long curr_length = null;
      long curr = n;
      int curr_size = 8;
      long[] sequence = new long[curr_size];
      int curr_index = 0;
      sequence[curr_index] = curr;
      while (curr_length == null && curr != 1) {
        curr = collatz_next(curr);

        // Add to sequence
        curr_index++; // Increment index
        if (curr_index == curr_size) {
          curr_size *= 2;
          sequence = Arrays.copyOf(sequence, curr_size);
        }
        sequence[curr_index] = curr;

        if (hash_ != null) {
          curr_length = hash_.get(curr); // Can be null, no worries
        }
      }

      if (curr_length == null) {
        curr_length = (long) 1; // We know curr == 1
      }

      // if sequence[curr_index] has length curr_length, then sequence[0]
      // has length (curr_length + curr_index). Any total length over 200
      // should be stored in the hash.
      Long length_at_sequence = curr_index + curr_length;
      Long index_at_length = (long) 0;
      if (length_at_sequence > 200) {
        hash_.put(index_at_length, length_at_sequence);
        index_at_length++;
        length_at_sequence--;
      }
      return (curr_index + curr_length);
    }
  }

  public static long[] max_collatz_length_up_to_n(int n, HashMap<Long, Long> hash_) {
    long max_length = -1;
    long max_length_at = -1;
    long curr_length;

    for (int i = 1; i < n + 1; i++) {
      curr_length = length(i, hash_);
      if (curr_length > max_length) {
        max_length = curr_length;
        max_length_at = i;
      }
    }

    return new long[] {max_length_at, max_length};
  }

  public static long[] max_collatz_length_up_to_n(int n) {
    // TODO: Find better way to do this
    HashMap<Long, Long> hash_ = new HashMap<Long, Long>();
    hash_.put((long) 1, (long) 1);
    return max_collatz_length_up_to_n(n, hash_);
  }

  public static String main(boolean verbose) {
    long[] ans = max_collatz_length_up_to_n(999999);
    if (verbose) {
      String result = ans[0] + ".\nThe Collatz chain at ";
      result += ans[0] + " has length ";
      result += ans[1] + ".";
      return result;
    } else {
      return Long.toString(ans[0]);
    }
  }

  public static String main() {
    return main(false);
  }

  public static void main(String[] args) {
    System.out.println(main(true));
  }
}
