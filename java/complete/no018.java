import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.HashMap;

class no018 {
  public static String get_data() {
    String contents = "";
    try {
      String data_path = "/Users/dhermes/dhermes-project-euler/problem_data/";
      FileReader input = new FileReader(data_path + "no018.txt");
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

  public static int max_sum(int[][] triangle_matrix) {
    int max_depth = triangle_matrix.length - 1;

    // Set bottom row for memoization
    int depth = max_depth;
    HashMap<String, Integer> result = new HashMap();

    int entry;
    for (int i = 0; i < triangle_matrix[depth].length; i++) {
      entry = triangle_matrix[depth][i];
      result.put(i + "," + (max_depth - depth), entry);
    }
    depth--;

    // Set each row moving up the triangle based on
    // the results one low below
    int val_left, val_right;
    while (depth >= 0) {
      for (int i = 0; i < triangle_matrix[depth].length; i++) {
        entry = triangle_matrix[depth][i];
	val_left = result.get(i + "," + (max_depth - depth - 1));
	val_right = result.get(i + 1 + "," + (max_depth - depth - 1));
        result.put(i + "," +  (max_depth - depth),
                   entry + Math.max(val_left, val_right));
      }
      depth--;
    }

    return result.get(0 + "," + (max_depth - depth - 1));
  }

  public static int main(boolean verbose) {
    String triangle = get_data().trim();
    String[] triangle_split = triangle.split("\n");
    int[][] TRIANGLE_MAT = new int[triangle_split.length][];

    String[] line_split;
    int[] line_as_int;
    for (int i = 0; i < triangle_split.length; i++) {
      line_split = triangle_split[i].split(" ");
      line_as_int = new int[line_split.length];
      for (int j = 0; j < line_split.length; j++) {
        line_as_int[j] = Integer.parseInt(line_split[j]);
      }
      TRIANGLE_MAT[i] = line_as_int;
    }

    return max_sum(TRIANGLE_MAT);
  }

  public static int main() {
    return main(false);
  }

  public static void main(String[] args) {
    System.out.println(main(true));
  }
}
