import asyncio
import aiohttp

from time import perf_counter
from config.scraper_config import TOTAL_REQUESTS_COUNT

async def fetch_data(session, item_no):
    r = await session.get(f"http://127.0.0.1:8000/products/{item_no}")
    print(await r.json())


async def main():
    async with aiohttp.ClientSession() as session:
        products = [] # List of tasks
        for item_no in range(1, TOTAL_REQUESTS_COUNT + 1):
            products.append(fetch_data(session, item_no)) # Collecting tasks
        await asyncio.gather(*products) # Running all tasks concurrently


start = perf_counter()

asyncio.run(main())

stop = perf_counter()
print(f"Time taken : {stop - start}")
