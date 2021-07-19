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
README_PATH = os.getcwd() + '/READMES'
REPO_PATH = 'textfiles/repo_names'
REPO_PATH2 = 'textfiles/repo_names2'
CANDS_PATH = 'textfiles/CANDIDATES/'
TRASH_PATH = 'textfiles/TRASH/'

# NOTE: Keyword lists:
KEYWORDS = ['machine learning', 'artificial intelligence',
            'ai', 'ml', 'deep learning', 'neural net']
TOPICS = ['machine-learning', 'artificial-intelligence',
          'deeplearning', 'deep-learning',
          'machinelearning', 'neural-networks',
          'neural-network']


# Get metadata from a repo given its modified repo name,
# in the format owner_reponame.txt.
def metadata(mod_repo_name):
    fptr = open(f'METADATA/{mod_repo_name}')
    meta = dict()
    for line in fptr.readlines():
        k, v = tuple(line.split(':', 1))
        meta[k] = v
    return meta


# This function goes through the description searching for
# keywords indicative of ML/AI.
# TRUE: passes filter.
# FALSE: fails filter.
def desc_filter(desc: str) -> bool:
    if desc is None:
        return False
    else:
        return True if any(kw in desc for kw in KEYWORDS) else False


# This function goes through topics looking for words
# indicative of ML/AI.
# TRUE: passes filter.
# FALSE: fails filter.
def topic_filter(topics: str) -> bool:
    if topics is None or len(topics) == 0:
        return False
    else:
        return True if any(kw in topics for kw in TOPICS) else False

# This function goes through READMEs to search for
# sign of machine learning.
# TRUE: passes filter.
# FALSE: fails filter.
def README_filter(README: str) -> bool:
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

        file_cands = open('textfiles/CANDIDATES/candidates', 'w')
        file_trash = open('textfiles/TRASH/trash', 'w')

        # NOTE: Go through each slug in the repo_names file:
        for filename in curr_file.readlines():

            # Initial path here; will be added on to later:
            mod_repo_name = (filename.strip()).replace('/', '_') + '.txt'
            details = metadata(mod_repo_name)

            if len(details) != 8:
                print(f'{filename.strip()} has no metadata.')
                file_trash.write(filename)
                continue

            # TODO: Here we will run the filters.
            if desc_filter(details['description']):
                file_cands.write(filename)
            elif topic_filter(details['topics']):
                file_cands.write(filename)
            # elif README_filter(details['full_name']):
            #     file_cands.write(filename)
            else:
                file_trash.write(filename)

            # try:
            #     # First, make sure the repo is actually some sort
            #     # of project and not a paper or list.
            #     dest_path += ''
            #
            # except github.GithubException as g_err:
            #     if g_err.status == 404:
            #         print('README not found, moving on.')
            #     elif g_err.status == 403:
            #         print('Rate Limit Exceeded (GitHub)')
            #         print('5000 req/hr max.')
            #         exit(1)

        file_cands.close()
        file_trash.close()

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
                dest_path += ''

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
