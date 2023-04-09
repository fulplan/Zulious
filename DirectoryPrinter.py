import os
import pandas as pd
from termcolor import colored


class DirectoryPrinter:
    """
    This class contains the functionality for printing the valid directories found during the search process in beautiful colored text along with the response domain.
    """

    def __init__(self):
        self.valid_directories = []

    def print_valid_directories(self):
        """
        This method prints the valid directories found during the search process in beautiful colored text along with the response domain.
        """
        for directory in self.valid_directories:
            domain = self.extract_domain(directory)
            colored_directory = colored(directory, 'green')
            colored_domain = colored(domain, 'cyan')
            print("{} -> {}".format(colored_directory, colored_domain))

    def extract_domain(self, url):
        """
        This method extracts the domain from a URL.
        """
        return os.path.splitext(url)[1]

    def add_valid_directory(self, directory):
        """
        This method adds a valid directory to the list of valid directories.
        """
        self.valid_directories.append(directory)

    def print_directory_table(self):
        """
        This method outputs the valid directories found in a pretty Python table.
        """
        df = pd.DataFrame(self.valid_directories,
                          columns=["Valid Directories"])
        print(df.to_string(index=False))
        print("Total Valid Directories: {}".format(len(self.valid_directories)))

        """
        To use this class in other code, simply import it and create an instance of the DirectoryPrinter class. 
        Then call the add_valid_directory() method for each valid directory found during the search process. 
        Finally, call either the print_valid_directories() method to print the directories in colored text or 
        the print_directory_table() method to output the results in a pretty Python table:
        """


# from DirectoryPrinter import DirectoryPrinter

# # Create an instance of the DirectoryPrinter class
# printer = DirectoryPrinter()

# # Example list of valid directories found during search process
# valid_directories = ['/var/www/html/index.php', '/var/www/html/style.css', '/var/www/html/images/background.jpg']

# # Add each valid directory to the list
# for directory in valid_directories:
#     printer.add_valid_directory(directory)

# # Print the valid directories in colored text
# printer.print_valid_directories()

# # Output the results in a pretty Python table
# printer.print_directory_table()

"""
This will print the valid directories in colored text and output the results in a pretty Python table. 
You can modify the code to use your own list of valid directories to analyze.
"""
