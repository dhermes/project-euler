import java.math.BigInteger;

class no025 {
  public static int main(boolean verbose) {
    int fib_index = 1;
    BigInteger last = new BigInteger("0");
    BigInteger curr = new BigInteger("1");
    BigInteger tmp;

    while (curr.toString().length() < 1000) {
      tmp = curr.add(last);
      last = curr;
      curr = tmp;
      fib_index++;
    }

    return fib_index;
  }

  public static int main() {
    return main(false);
  }

  public static void main(String[] args) {
    System.out.println(main(true));
  }
}
