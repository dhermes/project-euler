import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.math.BigInteger;

class no013 {
  public static String get_data() {
    String contents = "";
    try {
      String data_path = "/Users/dhermes/dhermes-project-euler/problem_data/";
      FileReader input = new FileReader(data_path + "no013.txt");
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

  public static String main(boolean verbose) {
    String number = get_data();
    String[] numbers = number.split("\n");

    BigInteger total = BigInteger.valueOf(0);
    for (int i = 0; i < numbers.length; i++) {
      total = total.add(new BigInteger(numbers[i]));
    }

    return total.toString().substring(0, 10);
  }

  public static String main() {
    return main(false);
  }

  public static void main(String[] args) {
    System.out.println(main(true));
  }
}
