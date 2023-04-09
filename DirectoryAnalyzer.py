import urllib3
from collections import defaultdict


class DirectoryAnalyzer:
    """
    This class contains the functionality for post-search analysis of the directories found during the search process.
    """

    def __init__(self):
        self.http = urllib3.PoolManager()

    def analyze_directories(self, directories):
        """
        This method analyzes a list of directories and outputs statistics on the directories found.
        """
        total_directories = len(directories)
        extensions_count = defaultdict(int)

        for directory in directories:
            extension = directory.split('.')[-1]
            extensions_count[extension] += 1

        print("Total Directories: {}".format(total_directories))
        print("Directory Extensions:")

        for extension, count in extensions_count.items():
            print("{}: {}".format(extension, count))

    def make_http_request(self, url):
        """
        This method makes an HTTP/HTTPS request to the given URL.
        """
        response = self.http.request('GET', url)
        return response.data.decode('utf-8')

        """
        To use this class in other code, simply import it and create an instance of the DirectoryAnalyzer class. 
        Then call the analyze_directories() method and pass in a list of directories to analyze. 
        You can also use the make_http_request() method to make HTTP/HTTPS requests:
        """


# from DirectoryAnalyzer import DirectoryAnalyzer

# # Create an instance of the DirectoryAnalyzer class
# analyzer = DirectoryAnalyzer()

# # Example list of directories
# directories = ['/var/www/html/index.php', '/var/www/html/style.css', '/var/www/html/images/background.jpg']

# # Analyze the list of directories
# analyzer.analyze_directories(directories)

# # Make an HTTP/HTTPS request
# response = analyzer.make_http_request('https://www.google.com')
# print(response)


"""
This will output statistics on the list of directories and make an HTTP/HTTPS request to Google's homepage. 
You can modify the code to use your own list of directories and URLs to analyze.
"""
