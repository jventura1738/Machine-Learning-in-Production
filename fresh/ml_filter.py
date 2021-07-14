# Justin Ventura | Carnegie Mellon University

import os

"""
This file filters out repos which do not contain some sort of
machine learning aspect.

Heuristics:
"""

README_PATH = os.getcwd() + '\READMES'
REPO_PATH = 'textfiles/repo_names'
REPO_PATH2 = 'textfiles/repo_names2'
KEYWORDS = ['machine learning', 'artificial intelligence',
            'ai', 'ml', 'deep learning', 'neural net']
TOPICS = ['machine-learning', 'artificial-intelligence',
          'ai', 'ml', 'deeplearning', 'deep-learning',
          'machinelearning', 'neural-networks',
          'neural-network']


# This function goes through READMEs to search for
# sign of machine learning.
def README_filter():
    pass


def desc_filter():
    pass


def topic_filter():
    pass


# Main function:
def _main():

    # # Loop through each file in the
    # for filename in os.listdir(README_PATH):
    #     with open(os.path.join(README_PATH, filename), 'r') as f:
    #         print(f.name)

    dest_file = open(REPO_PATH2, 'a')
    curr_file = open(REPO_PATH, 'r')
    for filename in curr_file.readlines():
        print(filename)

        # TODO: Here we will run the filters.
        README_filter()

# Run script directly:
if __name__ == '__main__':
    _main()
