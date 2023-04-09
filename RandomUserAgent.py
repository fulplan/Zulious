import random
from fake_useragent import UserAgent


class RandomUserAgent:
    """
    This class contains the functionality for generating a random user agent to use during the search process.
    """

    def __init__(self, ua=None, wordlist=None):
        self.ua = ua
        self.wordlist = wordlist

    def get_user_agent(self):
        """
        This method generates a random user agent or returns the specified user agent.
        """
        if self.ua is None and self.wordlist is None:
            ua = UserAgent()
            return ua.random
        elif self.ua is not None:
            return self.ua
        elif self.wordlist is not None:
            with open(self.wordlist) as f:
                lines = f.readlines()
            return random.choice(lines).strip()

        """
        With these modifications, the RandomUserAgent class now accepts two optional arguments: 
        ua and wordlist. If ua is provided, the specified user agent will be used during the search process. 
        If wordlist is provided, the class will read in a list of user agents from the file at the path specified 
        by wordlist and randomly choose one to use during the search process.
        
        
        To use this updated class, simply create an instance of the RandomUserAgent class and optionally provide values for ua and/or wordlist. 
        Then, call the get_user_agent() method to generate a user agent for use during the search process. For example:
        """

# # Create an instance of the RandomUserAgent class with a specified user agent
# rua = RandomUserAgent(ua='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')

# # Create an instance of the RandomUserAgent class with a wordlist of user agents
# rua_wordlist = RandomUserAgent(wordlist='user_agents.txt')

# # Generate a random user agent
# random_ua = rua.get_user_agent()

# # Use a specified user agent
# specific_ua = rua.get_user_agent()

# # Use a user agent from a wordlist
# wordlist_ua = rua_wordlist.get_user_agent()

    """
    This will create two instances of the RandomUserAgent class: one with a specified user agent and one with a wordlist of user agents. 
    Then, it will generate a random user agent using the first instance, use the specified user agent using the first instance, and use a user agent 
    from the wordlist using the second instance.
    """
