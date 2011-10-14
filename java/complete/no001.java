class no001 {
  public static int main(boolean verbose) {
    int result = 0;
    for (int i = 1; i < 1000; i++) {
      if (i % 3 == 0 || i % 5 == 0) {
        result += i;
      }
    }
    return result;
  }

  public static int main() {
    return main(false);
  }

  public static void main(String[] args) {
    System.out.println(main());
  }
}
