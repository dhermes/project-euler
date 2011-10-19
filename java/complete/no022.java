import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Arrays;

class no022 {
  public static String get_data() {
    String contents = "";
    try {
      String data_path = "/Users/dhermes/dhermes-project-euler/problem_data/";
      FileReader input = new FileReader(data_path + "no022.txt");
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

  public static int name_score(String name) {
    int result = 0;
    for (int i = 0; i < name.length(); i++) {
      result += (Character.toUpperCase(name.charAt(i)) - 'A') + 1;
    }
    return result;
  }

  public static int main(boolean verbose) {
    String data = get_data();
    String[] names = data.substring(1, data.length() - 2).split("\",\"");
    Arrays.sort(names);

    int result = 0;
    for (int i = 0; i < names.length; i++) {
      result += name_score(names[i]) * (i + 1);
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
