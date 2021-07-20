# Justin Ventura | Carnegie Mellon University

import os
import time

"""
This file clones a repository temporarily to do a small analysis
on the code in order to see if there is some sort of ML/AI.
"""

PATH_TO_METADATA = 'METADATA/'


# Clone the repository given the metadata file:
def clone_repo(mod_repo_name: str) -> None:
    try:
        fptr = open(PATH_TO_METADATA, 'r')
    except FileNotFoundError:
        print(f'{mod_repo_name}.txt does not exist.')
        time.sleep(5)


# NOTE: Main function for testing:
def _main():
    pass


# Run script directly:
if __name__ == '__main__':
    _main()