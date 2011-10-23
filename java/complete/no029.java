import java.math.BigInteger;
import java.util.HashMap;

class no029 {
  public static int main(boolean verbose) {
    int n = 100;
    HashMap<BigInteger, Boolean> powers = new HashMap<BigInteger, Boolean>();
    for (int base = 2; base < n + 1; base++) {
      BigInteger base_as_big_int = BigInteger.valueOf(base);
      for (int exponent = 2; exponent < n + 1; exponent++) {
        powers.put(base_as_big_int.pow(exponent), true);
      }
    }

    return powers.keySet().size();
  }

  public static int main() {
    return main(false);
  }

  public static void main(String[] args) {
    System.out.println(main(true));
  }
}
