class no028 {
  public static int spiral_sum(int n) throws Exception {
    if (n % 2 == 0) {
      throw new Exception("Spiral only occurs on odds.");
    }

    int curr_val = 1;
    int total = 0;

    // as we move along the corners on the spiral, the number of
    // steps (i.e. number of corners) dictates the size of each
    // new step. In almost all cases, the step increases by one
    // but every four, when the next corner wraps a new layer,
    // it does not increase
    int step_num = 0;
    int step_size = 0;
    while (curr_val <= n * n) {
      if (step_num % 2 == 0) {
        step_size++;
      }
      curr_val += step_size;

      total += curr_val;
      if (step_num % 4 == 0) {
        total--;
      }
      step_num++;
    }

    return total;
  }

  public static int main(boolean verbose) {
    try {
      return spiral_sum(1001);
    } catch (Exception exc) {
      exc.printStackTrace();
      return -1;
    }
  }

  public static int main() {
    return main(false);
  }

  public static void main(String[] args) {
    System.out.println(main(true));
  }
}
