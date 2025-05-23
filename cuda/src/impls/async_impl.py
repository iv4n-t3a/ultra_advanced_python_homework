import asyncio
from common import is_prime_async


async def find_primes_async_helper(nums):
    tasks = [is_prime_async(num) for num in nums]
    res = await asyncio.gather(*tasks)
    return res


def find_primes_async(nums):
    return asyncio.run(find_primes_async_helper(nums))
