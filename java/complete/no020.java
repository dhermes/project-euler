import java.math.BigInteger;

class no020 {
  public static BigInteger factorial(int n) {
    if (n < 2) {
      return new BigInteger("1");
    } else {
      return factorial(n - 1).multiply(new BigInteger(Integer.toString(n)));
    }
  }

  public static int main(boolean verbose) {
    BigInteger val = factorial(100);

    String val_as_str = val.toString();
    int result = 0;
    for (int i = 0; i < val_as_str.length(); i++) {
      result += Integer.parseInt(Character.toString(val_as_str.charAt(i)));
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
