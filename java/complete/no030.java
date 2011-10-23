import java.util.Arrays;

class no030 {
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

  public static String join(String join_val, int[] arr) {
    String result = "";
    int length = arr.length;
    for (int i = 0; i < length - 1; i++) {
      result += Integer.toString(arr[i]) + join_val;
    }

    if (length > 0) {
      result += Integer.toString(arr[length - 1]);
    }

    return result;
  }

  public static int sum_of_digits_powers(int n, int power) {
    int result = 0;
    int left_most_n = n;
    while (left_most_n != 0) {
      result += (int) Math.pow(left_most_n % 10, power);
      left_most_n /= 10; // Integer division intended
    }
    return result;
  }

  public static String main(boolean verbose) {
    int curr_size = 8;
    int[] valid = new int[curr_size];
    int curr_index = 0;
    for (int i = 2; i < 999999 + 1; i++) {
      if (sum_of_digits_powers(i, 5) == i) {
        if (curr_index == curr_size) {
          curr_size *= 2;
          valid = Arrays.copyOf(valid, curr_size);
        }

        valid[curr_index] = i;
        curr_index++;
      }
    }
    valid = Arrays.copyOf(valid, curr_index);

    String result = Integer.toString(array_sum(valid));
    if (verbose) {
      result += ".\nThe numbers satisfying this property are: ";
      result += join(", ", valid) + ".";
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
