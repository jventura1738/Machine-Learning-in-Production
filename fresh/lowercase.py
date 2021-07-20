# Justin Ventura | Carnegie Mellon University

import os
import sys

"""
This script is for converting text to lowercase, for now
it takes all files in a directory, then goes through each
word, replacing all uppercase with lowercase.
"""


# Main function:
def _main():
    assert(len(sys.argv) == 2), 'Expected directory name as argument.'
    dir_name = sys.argv[1]
    dir_list = os.listdir(dir_name)

    for file in dir_list:
        with open(f'{dir_name}/{file}', 'r') as infile:
            content = infile.read()
        with open(f'{dir_name}/{file}', 'w') as outfile:
            outfile.write(content.lower())


# Run script directly:
if __name__ == '__main__':
    _main()
