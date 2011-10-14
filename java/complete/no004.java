import java.util.Arrays;

class no004 {
  public static boolean is_palindrome(String str) {
    if (str.length() < 2) {
      return true;
    } else if (str.charAt(0) != str.charAt(str.length() - 1)) {
      return false;
    }

    return is_palindrome(str.substring(1, str.length() - 1));
  }

  public static boolean is_palindrome(int val) {
    return is_palindrome(Integer.toString(val));
  }

  public static int main(boolean verbose) {
    int best = 0;
    for (int i = 100; i < 1000; i++) {
      for (int j = i; j < 1000; j++) {
        if (is_palindrome(i * j)) {
          best = Math.max(best, i * j);
        }
      }
    }
    return best;
  }

  public static int main() {
    return main(false);
  }

  public static void main(String[] args) {
    System.out.println(main());
  }
}
