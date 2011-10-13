abstract class Benchmark {
  abstract void benchmark();

  public final long repeat(int count) {
    long start = System.nanoTime();
    for (int i = 0; i < count; i++) {
      benchmark();
    }
    return (System.nanoTime() - start);
    }
}

class MethodBenchmark extends Benchmark {
  /** Do nothing, just return. */
  void benchmark() {
  }

  public static void main(String[] args) {
    int count = Integer.parseInt(args[0]);
    long time = new MethodBenchmark().repeat(count);
    System.out.println(count + " methods in " +
                       time + " nanoseconds");
  }
}
