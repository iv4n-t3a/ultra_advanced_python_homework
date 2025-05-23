from multiprocessing import Pool
from common import is_prime


def find_primes_multiprocessing(nums):
    with Pool() as pool:
        res = pool.map(is_prime, nums)
    return res
