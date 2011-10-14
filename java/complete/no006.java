class no006 {
  public static int polygonal_number(int s, int n) {
    return n * ((s - 2) * n - (s - 4)) / 2;
  }

  public static int sum_first_n_sq(int n) {
    return (n * (n + 1) * (2 * n + 1)) / 6;
  }

  public static int main(boolean verbose) {
    int poly_val = polygonal_number(3, 100);
    return Math.abs(sum_first_n_sq(100) - poly_val * poly_val);
  }

  public static int main() {
    return main(false);
  }

  public static void main(String[] args) {
    System.out.println(main());
  }
}
