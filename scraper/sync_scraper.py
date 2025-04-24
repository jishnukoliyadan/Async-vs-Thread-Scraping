import requests
from time import perf_counter
from config.scraper_config import TOTAL_REQUESTS_COUNT

start = perf_counter()

for item_no in range(1, TOTAL_REQUESTS_COUNT + 1):
    r = requests.get(f"http://127.0.0.1:8000/products/{item_no}")
    print(r.json())

stop = perf_counter()
print(f"Time taken : {stop - start}")
