class no009 {
  public static int [] first_triplet(int total) {
    int c;
    for (int a = 1; a < total - 1; a++) {
      for (int b = 1; b < total - a; b++) {
        c = total - a - b;
        if (a * a + b * b == c * c) {
          return new int[] {a, b, c};
        }
      }
    }

    return new int[0];
  }

  public static int main(boolean verbose) {
    int [] triplet = first_triplet(1000);
    // In future, use reduce to multiply
    return triplet[0] * triplet[1] * triplet[2];
  }

  public static int main() {
    return main(false);
  }

  public static void main(String[] args) {
    System.out.println(main());
  }
}
