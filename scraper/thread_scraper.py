import requests
from time import perf_counter
from config.scraper_config import TOTAL_REQUESTS_COUNT
from concurrent.futures import ThreadPoolExecutor


def get_data(item_no):
    r = requests.get(f"http://127.0.0.1:8000/products/{item_no}")
    print(r.json())


start = perf_counter()

with ThreadPoolExecutor() as executor:
    executor.map(get_data, range(1, TOTAL_REQUESTS_COUNT + 1))

stop = perf_counter()
print(f"Time taken : {stop - start}")
