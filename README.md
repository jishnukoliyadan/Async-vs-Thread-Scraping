# Async vs Thread Scraping

This project compares the efficiency and performance of different methods for making HTTP requests in Python for web scraping purposes. Specifically, it compares :

1. **A normal for-loop** to iterate over each link sequentially.
2. **Asyncio** for asynchronous requests using AIOHttp.
3. **Python ThreadPoolExecutor** to manage multiple threads for making concurrent requests.

The goal is to understand how these different methods perform when making several thousand HTTP requests, and how each method scales in terms of speed and efficiency.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

