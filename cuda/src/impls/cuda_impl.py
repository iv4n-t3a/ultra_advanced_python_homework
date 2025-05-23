from numba import cuda
from common import is_prime_cuda

import numpy as np
import math


@cuda.jit
def find_primes_kernel(io_array):
    pos = cuda.grid(1)

    if pos < io_array.size:
        num = io_array[pos]
        for i in range(2, math.ceil(num**0.5)):
            if num % i == 0:
                io_array[pos] = 0
                return
        io_array[pos] = 1


THREADSPERBLOCK = 256


def find_primes_cuda(arr):
    blockspergrid = len(arr) // THREADSPERBLOCK + 1
    find_primes_kernel[blockspergrid, THREADSPERBLOCK](arr)
    return arr
