# Is-It-Prime

> How do we quickly know a number is prime?

This project explores and compares different algorithms for primality testing, ranging from classical methods to probabilistic and theoretical approaches. The goal is to understand both correctness and performance trade-offs in practical implementations.

### Benchmarking

The project includes benchmark tests to compare performance across different primality testing methods. The Mersenne number M61 = 2^61 - 1 is used as a standard performance benchmark. The results of the experiments are shown in the screenshot below.

![benchmark](./wiki/2026-07-05%2000.53.44.png)

Run benchmarks with:

```sh
pytest test/test_benchmark.py -v --durations=0
```