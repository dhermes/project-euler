class no019 {
  public static boolean leap_year(int year) {
    if (year % 4 == 0) {
      if (year % 100 == 0) {
        return (year % 400 == 0);
      } else {
        return true;
      }
    } else {
      return false;
    }
  }

  public static int[] month_lengths(int year) {
    int [] result = new int[] {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    if (leap_year(year)) {
      result[1] = 29;
    }
    return result;
  }

  public static int main(boolean verbose) {
    // We call the days of the week 0 - Sunday,...,6 - Saturday modulo 7
    // 1 Jan 1900 was a Monday. i.e. equal to 1
    int first_year_sum = 0;
    int[] lengths = month_lengths(1900);
    for (int i = 0; i < lengths.length; i++) {
      first_year_sum += lengths[i];
    }
    int jan_1_1901 = (1 + first_year_sum) % 7;

    int date = jan_1_1901;
    int count = 0;
    if (date == 0) {
	count++;
    }

    int[] months;
    int month;
    for (int year = 1901; year < 2001; year++) {
      months = month_lengths(year);
      for (int i = 0; i < months.length; i++) {
        month = months[i];
        date = (date + month) % 7;
        if (date == 0) {
          count++;
        }
      }
    }

    // The final date will be Jan 1 2001, so we need to
    // disallow it if it was bad
    if (date == 0) {
        count--;
    }
    return count;
  }

  public static int main() {
    return main(false);
  }

  public static void main(String[] args) {
    System.out.println(main(true));
  }
}
