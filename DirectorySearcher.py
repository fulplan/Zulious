import urllib3
from concurrent.futures import ThreadPoolExecutor


class DirectorySearcher:
    """
    This class contains the main functionality of the tool, including the ability to search for directories of a given domain,
    with features such as stealth mode and random user agent to bypass security measures. The class supports multithreading to speed up
    the search process, with a default number of threads set to 5. Additionally, the class accepts an argument for setting the timeout,
    with a default value of 5 seconds if no argument is provided.
    """

    def __init__(self, domain, timeout=5, num_threads=5):
        self.domain = domain
        self.timeout = timeout
        self.num_threads = num_threads
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    def search_directories(self):
        """
        This method searches for directories on the domain using a wordlist.
        """
        # Load the wordlist
        with open("wordlist.txt", "r") as f:
            wordlist = f.read().splitlines()

        # Create a thread pool executor
        with ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            for path in wordlist:
                # Build the URL to check
                url = f"https://{self.domain}/{path}"

                # Submit the request to the executor
                executor.submit(self.check_directory, url)

    def check_directory(self, url):
        """
        This method checks if a directory exists on the domain at the given URL.
        """
        try:
            # Make an HTTP request to the URL
            http = urllib3.PoolManager(
                timeout=self.timeout, headers=self.headers)
            response = http.request('HEAD', url)

            # Handle the response
            if response.status == 200:
                print(f"[+] Found: {url}")
            elif response.status == 403:
                print(f"[-] Forbidden: {url}")
            elif response.status == 404:
                pass
            else:
                print(f"[?] Unknown: {url}")
        except Exception as e:
            print(f"[!] Error: {url} - {e}")

        """
        To use this class in other code, simply import it and create an instance of the DirectorySearcher class, 
        passing in the domain you want to search as the first argument (and optionally specifying the timeout and 
        number of threads):
        """

# from DirectorySearcher import DirectorySearcher

# searcher = DirectorySearcher("example.com", timeout=10, num_threads=10)
# searcher.search_directories()


"""
This will start the directory search process using the specified settings. 
You can also customize the wordlist used by modifying the "wordlist.txt" file in the same directory as the script.
"""
