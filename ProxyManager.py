import socks
import urllib3


class ProxyManager:
    """
    This class contains the functionality for managing SOCKS or Tor proxy usage.
    """

    def __init__(self, proxy_ip=None, proxy_port=None, proxy_username=None, proxy_password=None, proxy_type='http'):
        self.proxy_ip = proxy_ip
        self.proxy_port = proxy_port
        self.proxy_username = proxy_username
        self.proxy_password = proxy_password
        self.proxy_type = proxy_type

        # Set up proxy manager
        if self.proxy_ip is not None and self.proxy_port is not None:
            self.proxy_url = '{}://{}:{}'.format(
                self.proxy_type, self.proxy_ip, self.proxy_port)
            proxy_auth = None
            if self.proxy_username is not None and self.proxy_password is not None:
                proxy_auth = urllib3.util.make_headers(
                    proxy_basic_auth='{}:{}'.format(self.proxy_username, self.proxy_password))
            self.proxy_manager = urllib3.ProxyManager(
                proxy_url=self.proxy_url, proxy_headers=proxy_auth, timeout=urllib3.Timeout(connect=5.0, read=10.0))

    def make_request(self, url):
        """
        This method makes a request using urllib3 with the specified proxy settings.
        """
        if self.proxy_ip is not None and self.proxy_port is not None:
            return self.proxy_manager.request('GET', url)
        else:
            return urllib3.PoolManager().request('GET', url)

    def use_tor(self):
        """
        This method sets up a connection to Tor for proxy usage.
        """
        socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
        socket.socket = socks.socksocket


"""
To use this class in other code, simply import it and create an instance of the ProxyManager class. 
Then call the make_request() method with the desired URL to make a request using the specified proxy settings. 
Additionally, you can call the use_tor() method to set up a connection to Tor for proxy usage:
"""


# from ProxyManager import ProxyManager

# # Create an instance of the ProxyManager class
# manager = ProxyManager(proxy_ip='123.45.67.89', proxy_port=8080, proxy_username='user', proxy_password='pass')

# # Make a request using the specified proxy settings
# response = manager.make_request('https://www.google.com')

# # Print the response
# print(response.data.decode())

# # Set up a connection to Tor for proxy usage
# manager.use_tor()

# # Make a request using Tor for proxy usage
# response = manager.make_request('https://www.google.com')

# # Print the response
# print(response.data.decode())


"""
This will make a request using the specified proxy settings, print the response, 
set up a connection to Tor for proxy usage, make a request using Tor for proxy usage, and print the response. 
You can modify the code to include your own proxy settings and URLs to request.
"""
