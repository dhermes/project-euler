class no002 {
  public static int[] recurrence_next(int[] relation, int[] values) throws Exception {
    if (relation == null || values == null || relation.length != values.length) {
      throw new Exception("Poorly specified recurrence");
    }
    int recurrence_order = relation.length;
    int next_val = 0;
    for (int i = 0; i < recurrence_order; i++) {
      next_val += relation[i] * values[i];
    }

    // May be possible to speed this up with java.util.Arrays.copyOfRange
    int[] result = new int[recurrence_order];
    for (int i = 1; i < recurrence_order; i++) {
      result[i - 1] = values[i];
    }
    result[recurrence_order - 1] = next_val;

    return result;
  }

  public static int main(boolean verbose) throws Exception {
    int a = 0;
    int b = 2;
    int running_sum = 0;
    int[] recurrence = new int[] {1, 4};
    int[] values = new int[] {a, b};
    while (b <= 4000000) {
      running_sum += b;
      // Do I need a try/catch here or will main catch it?
      values = recurrence_next(recurrence, values);
      a = values[0];
      b = values[1];
    }
    return running_sum;
  }

  public static int main() throws Exception {
    return main(false);
  }

  public static void main(String[] args) { 
    try {
      System.out.println(main());
    } catch (Exception exc) {
      exc.printStackTrace();
    }   
  }
}
