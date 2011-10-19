class no017 {
  public static String join(String join_val, String[] arr) {
    String result = "";
    int length = arr.length;
    for (int i = 0; i < length - 1; i++) {
      result += arr[i] + join_val;
    }

    if (length > 0) {
      result += arr[length - 1];
    }

    return result;
  }

  public static String words(int n) {
    String[] tens = new String[] {"zero_index_filler", "one_index_filler",
                                  "twenty", "thirty", "forty", "fifty", "sixty",
                                  "seventy",  "eighty", "ninety"};
    String[] teens = new String[] {"ten", "eleven", "twelve", "thirteen",
                                   "fourteen", "fifteen", "sixteen", "seventeen",
                                   "eighteen", "nineteen"};
    String[] ones = new String[] {"zero_index_filler", "one", "two", "three",
                                  "four", "five", "six", "seven",
                                  "eight", "nine"};

    if (n == 1000) {
      return "one thousand";
    }

    String result = "";
    int dig_units = n % 10;
    int dig_tens = ((n - dig_units) / 10) % 10;
    int dig_hundreds = ((n - 10 * dig_tens - dig_units) / 100) % 10;

    if (dig_hundreds != 0) {
      if (n != 100 * dig_hundreds) {
        result += " " + ones[dig_hundreds] + "hundred and";
      } else {
        return ones[dig_hundreds] + " hundred";
      }
    }

    if (dig_tens == 1) {
      result += " " + teens[dig_units]; // index ignores parts ten of n
      return result.trim(); // may have leading space
    } else if (dig_tens != 0) {
      result += " " + tens[dig_tens];
    }

    // Here we can safely ignore teens since we return in that loop
    if (dig_units != 0) {
      result += " " + ones[dig_units];
    }

    return result.trim(); // may have leading space
  }

  public static int num_letters_in_word(int n) {
    String result = words(n);
    result = join("", result.split(" "));
    result = join("", result.split("-"));
    return result.length();
  }

  public static int main(boolean verbose) {
    int result = 0;
    for (int i = 1; i <= 1000; i++) {
      result += num_letters_in_word(i);
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
