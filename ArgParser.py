# from ArgParser import ArgParser
import argparse


class ArgParser:
    """
    This class contains the functionality for parsing command line arguments using the argparse library.
    """

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description='Directory Search Tool')

        # Define the command line arguments
        self.parser.add_argument('-e', '--extensions',
                                 help='List of file extensions to search for (default: php, html, txt)',
                                 nargs='+', default=['php', 'html', 'txt'])
        self.parser.add_argument('-l', '--level',
                                 help='Search only for directories at a certain level')
        self.parser.add_argument('-x', '--exclude',
                                 help='Exclude directories matching a certain pattern')
        self.parser.add_argument('-r', '--analyze',
                                 help='Analyze search results after search', action='store_true')
        self.parser.add_argument('-o', '--output',
                                 help='Save valid directories to a file')

    def parse_args(self):
        """
        This method parses the command line arguments and returns them as an object.
        """
        return self.parser.parse_args()


"""
    To use this class in other code, simply import it and create an instance of the ArgParser class. 
    Then call the parse_args() method to parse the command line arguments
"""


# # Create an instance of the ArgParser class
# parser = ArgParser()

# # Parse the command line arguments
# args = parser.parse_args()

# # Access the parsed arguments
# print(args.extensions)
# print(args.level)
# print(args.exclude)
# print(args.analyze)
# print(args.output)

"""
This will print out the parsed command line arguments. 
You can modify the code to perform directory searches based on these arguments, as well 
as save the search results to a file if desired.
"""
