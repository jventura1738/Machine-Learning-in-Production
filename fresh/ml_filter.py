# Justin Ventura | Carnegie Mellon University

import os
import sys
import github

"""
This file filters out repos which do not contain some sort of
machine learning aspect.

Heuristics:
"""

# TODO: Need to clone repositories to test out filters.

# NOTE: Path variables
README_PATH = os.getcwd() + '\READMES'
REPO_PATH = 'textfiles/repo_names'
REPO_PATH2 = 'textfiles/repo_names2'

# NOTE: Keyword lists:
KEYWORDS = ['machine learning', 'artificial intelligence',
            'ai', 'ml', 'deep learning', 'neural net']
TOPICS = ['machine-learning', 'artificial-intelligence',
          'ai', 'ml', 'deeplearning', 'deep-learning',
          'machinelearning', 'neural-networks',
          'neural-network']


# Filters out papers, lists, etc.
def paper_filter() -> str:
    pass


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

    dest_file = open(REPO_PATH2, 'a')

    # If no additional arguments are passed into the
    # argument vector:
    if len(sys.argv) <= 1:
        print(f'Using file {REPO_PATH} to filter:')

        # NOTE: Collect all slugs:
        curr_file = open(REPO_PATH, 'r')

        # NOTE: Go through each slug in the repo_names file:
        for filename in curr_file.readlines():

            # Initial path here; will be added on to later:
            dest_path = 'textfiles/'

            # TODO: Here we will run the filters.
            try:
                # First, make sure the repo is actually some sort
                # of project and not a paper or list.
                dest_path += paper_filter()

            except github.GithubException as g_err:
                if g_err.status == 404:
                    print('README not found, moving on.')
                elif g_err.status == 403:
                    print('Rate Limit Exceeded (GitHub)')
                    print('5000 req/hr max.')
                    exit(1)

    # If the argument vector contains additional arguments:
    else:
        print('Using argument vector to filter:')

        # NOTE: Go through each slug in the argument vector:
        for filename in sys.argv[1:]:

            # Initial path here; will be added on to later:
            dest_path = 'textfiles/'

            # TODO: Here we will run the filters.
            try:
                # First, make sure the repo is actually some sort
                # of project and not a paper or list.
                dest_path += paper_filter()

            except github.GithubException as g_err:
                if g_err.status == 404:
                    print('README not found, moving on.')
                elif g_err.status == 403:
                    print('Rate Limit Exceeded (GitHub)')
                    print('5000 req/hr max.')
                    exit(1)


# Run script directly:
if __name__ == '__main__':
    _main()


# # Loop through each file in the
    # for filename in os.listdir(README_PATH):
    #     with open(os.path.join(README_PATH, filename), 'r') as f:
    #         print(f.name)