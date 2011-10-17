class no005 {
  public static long gcd(long a, long b) {
    long M = Math.max(a, b);
    long m = Math.min(a, b);

    if (m == 0) {
      return M;
    } else if (M == 0) {
      return m;
    } else if (M == m) {
      return M;
    }

    return gcd(m, M % m);
  }

  public static long min_product(long n) {
    if (n < 2) {
      return 1;
    }

    long prod = min_product(n - 1);
    long shared = gcd(prod, n);
    return (prod * n) / shared;
  }

  public static long main(boolean verbose) {
    return min_product(20);
  }

  public static long main() {
    return main(false);
  }

  public static void main(String[] args) {
    System.out.println(main(true));
  }
}
