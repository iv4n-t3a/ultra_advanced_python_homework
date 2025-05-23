from concurrent.futures import ThreadPoolExecutor
from common import is_prime

def find_primes_multithreaded(nums):
    res = [False] * len(nums)

    def check_prime(index, number):
        res[index] = is_prime(number)

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(check_prime, i, num) for i, num in enumerate(nums)]
        for future in futures:
            future.result()

    return res
