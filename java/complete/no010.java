import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;

class no010 {
  public static String get_data() {
    String contents = "";
    try {
      String data_path = "/Users/dhermes/dhermes-project-euler/problem_data/";
      FileReader input = new FileReader(data_path + "no008.txt");
      BufferedReader buffered_input =  new BufferedReader(input);
      try {
        String line;
        while ((line = buffered_input.readLine()) != null) {
          contents += line;
          contents += System.getProperty("line.separator");
        }
      } finally {
        buffered_input.close();
      }
    } catch (IOException exc) {
      exc.printStackTrace();
    }

    return contents;
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

  public static int product_consec_digits(String number, int consecutive) {
    int length = number.length();
    int[] digits = new int[length];
    for (int i = 0; i < length; i++) {
      digits[i] = Integer.parseInt(Character.toString(number.charAt(i)));
    }

    int ans = 0;
    int product;
    int max_start = length - consecutive;
    for (int i = 0; i <= max_start; i++) {
      product = 1;
      for (int j = 0; j < consecutive; j++) {
        product *= digits[i + j];
      }
      ans = Math.max(ans, product);
    }    

    return ans;
  }

  public static int main(boolean verbose) {
    String contents = join("", get_data().split("\n"));
    return product_consec_digits(contents, 5);
  }

  public static long main() {
    return main(false);
  }

  public static void main(String[] args) {
    System.out.println(main());
  }
}
