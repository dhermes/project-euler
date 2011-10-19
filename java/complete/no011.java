import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;

class no011 {
  public static String get_data() {
    String contents = "";
    try {
      String data_path = "/Users/dhermes/dhermes-project-euler/problem_data/";
      FileReader input = new FileReader(data_path + "no011.txt");
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

  public static int[][] make_path(int[] point, int[] step, int length) {
    int[][] result = new int[length][];
    for (int i = 0; i < length; i++) {
      result[i] = new int[] {point[0] + i * step[0], point[1] + i * step[1]};
    }
    return result;
  }

  public static int convert(int[][] path, int[][] data) {
    int result = 1;
    int x, y;
    for(int i = 0; i < path.length; i++) {
      x = path[i][0];
      y = path[i][1];
      result *= data[x][y];
    }
    return result;
  }

  public static int main(boolean verbose) {
    String DATA_str = get_data();
    String[] DATA_split = DATA_str.split("\n");
    int[][] DATA = new int[DATA_split.length][];

    String[] line_split;
    int[] line_as_int;
    for (int i = 0; i < DATA_split.length; i++) {
      line_split = DATA_split[i].split(" ");
      line_as_int = new int[line_split.length];
      for (int j = 0; j < line_split.length; j++) {
        line_as_int[j] = Integer.parseInt(line_split[j]);
      }
      DATA[i] = line_as_int;
    }

    // UP/DOWN goes from DATA[x][y] to DATA[x+3][y] where 0 <= x, x+3, y <= 19
    int vert = 0;
    for (int x = 0; x < 17; x++) {
      for (int y = 0; y < 20; y++) {
        vert = Math.max(vert,
            convert(make_path(new int[] {x, y}, new int[] {1, 0}, 4), DATA));
      }
    }

    // LEFT/RIGHT goes from DATA[x][y] to DATA[x][y+3] where 0 <= x, y, y+3 <= 19
    int horiz = 0;
    for (int x = 0; x < 20; x++) {
      for (int y = 0; y < 17; y++) {
        horiz = Math.max(horiz,
            convert(make_path(new int[] {x, y}, new int[] {0, 1}, 4), DATA));
      }
    }

    // DIAGONAL L->R goes from DATA[x][y] to DATA[x+3][y+3] via +[1,1]
    int diag_l_r = 0;
    for (int x = 0; x < 17; x++) {
      for (int y = 0; y < 17; y++) {
        diag_l_r = Math.max(diag_l_r,
            convert(make_path(new int[] {x, y}, new int[] {1, 1}, 4), DATA));
      }
    }

    // DIAGONAL R->L goes from DATA[x][y] to DATA[x-3][y+3] via +[-1,1]
    int diag_r_l = 0;
    for (int x = 3; x < 20; x++) {
      for (int y = 0; y < 17; y++) {
        diag_r_l = Math.max(diag_r_l,
            convert(make_path(new int[] {x, y}, new int[] {-1, 1}, 4), DATA));
      }
    }

    int result = Math.max(vert, horiz);
    result = Math.max(result, diag_l_r);
    result = Math.max(result, diag_r_l);
    return result;
  }

  public static int main() {
    return main(false);
  }

  public static void main(String[] args) {
    System.out.println(main(true));
  }
}
