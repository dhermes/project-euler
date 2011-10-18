import java.math.BigInteger;

class no015 {
  public static BigInteger factorial(int n) {
    if (n < 2) {
      return new BigInteger("1");
    } else {
      return factorial(n - 1).multiply(new BigInteger(Integer.toString(n)));
    }
  }

  public static BigInteger choose(int n, int k) {
    BigInteger result = factorial(n);
    result = result.divide(factorial(k));
    result = result.divide(factorial(n - k));
    return result;
  }

  public static BigInteger main(boolean verbose) {
    return choose(20 + 20, 20);
  }

  public static BigInteger main() {
    return main(false);
  }

  public static void main(String[] args) {
    System.out.println(main(true));
  }
}
