import java.math.BigInteger;

class no016 {
  public static int main(boolean verbose) {
    BigInteger val = (new BigInteger("2")).pow(1000);

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
