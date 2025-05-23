from impls.async_impl import find_primes_async
from impls.syncronized_impl import find_primes_syncronized
from impls.multithread_impl import find_primes_multithreaded
from impls.multiprocessing_impl import find_primes_multiprocessing
from impls.cuda_impl import find_primes_cuda

from random import random
from time import time
import numpy as np
import matplotlib.pyplot as plt
import os

benchmarked = [
    (find_primes_syncronized, "syncronized"),
    (find_primes_async, "async"),
    (find_primes_multithreaded, "multithread"),
    (find_primes_multiprocessing, "multiprocessing"),
    (find_primes_cuda, "cuda"),
]

sizes = [100, 1000, 5000, 10000, 20000, 100000]

def run_benchmarks():
    results = {name: [] for _, name in benchmarked}

    for size in sizes:
        arr = np.random.randint(2, 10**9, size)

        for f, name in benchmarked:
            print(f"running {name}({size} items)...")
            start = time()
            res = f(arr)
            end = time()
            assert len(res) == len(arr)
            duration = end - start
            results[name].append(duration)
            print(f"{name}({size} items) finished for {duration:.3f}")

    return results

def plot_results(results):
    for name, times in results.items():
        plt.plot(sizes, times, label=name)

    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (s)")
    plt.title("Benchmark Results")
    plt.legend()
    plt.grid(True)

    output_dir = "../assets/benchmark_results"
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "benchmark_results.png")
    plt.savefig(output_path)

    plt.show()

if __name__ == '__main__':
    results = run_benchmarks()
    plot_results(results)
