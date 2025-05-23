from common import is_prime

def find_primes_syncronized(nums):
    res = [False] * len(nums)
    for i, j in enumerate(nums):
        res[i] = is_prime(j)

    return res
