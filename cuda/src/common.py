import math
from numba import cuda


def is_prime(num):
    for i in range(2, math.ceil(num**0.5)):
        if num % i == 0:
            return False
    return True


async def is_prime_async(num):
    for i in range(2, math.ceil(num**0.5)):
        if num % i == 0:
            return False
    return True


@cuda.jit
def is_prime_cuda(num):
    for i in range(2, math.ceil(num**0.5)):
        if num % i == 0:
            return False
    return True
