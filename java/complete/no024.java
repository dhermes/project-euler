import java.math.BigInteger;

class no024 {
  public static BigInteger factorial(int n) {
    if (n < 2) {
      return new BigInteger("1");
    } else {
      return factorial(n - 1).multiply(new BigInteger(Integer.toString(n)));
    }
  }

  public static int[] lex(int[] list_, BigInteger perm) {
    if (list_.length < 2) {
      return list_.clone();
    }

    BigInteger curr_fact = factorial(list_.length - 1);
    BigInteger index_big = perm.divide(curr_fact); // int. division intended
    int index = Integer.parseInt(index_big.toString());
    BigInteger remaining = perm.mod(curr_fact);

    int[] sublist = new int[list_.length - 1];
    for (int i = 0; i < list_.length; i++) {
      if (i < index) {
        sublist[i] = list_[i];
      } else if (i > index) {
        sublist[i - 1] = list_[i];
      }
    }

    int[] sublist_shuffled = lex(sublist, remaining);
    int[] result = new int[list_.length];
    result[0] = list_[index];
    for (int i = 0; i < sublist_shuffled.length; i++) {
      result[i + 1] = sublist_shuffled[i];
    }
    return result;
  }

// def main(verbose=False):
//     list_ = range(10)
//     perm = 10**6 - 1 # Our indexing begins at 0
//     return "".join([str(dig) for dig in lex(list_, perm)])

  public static String main(boolean verbose) {
    int[] list_ = new int[10];
    for (int i = 0; i < 10; i++) {
      list_[i] = i;
    }
    BigInteger perm = BigInteger.valueOf((long) (Math.pow(10, 6) - 1));
    int[] shuffled = lex(list_, perm);

    String result = "";
    for (int i = 0; i < shuffled.length; i++) {
      result += shuffled[i];
    }
    return result;
  }

  public static String main() {
    return main(false);
  }

  public static void main(String[] args) {
    System.out.println(main(true));
  }
}
