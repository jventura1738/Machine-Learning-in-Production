# Justin Ventura | Carnegie Mellon University

import os
import sys
import time
import stscraper as scraper
from github import Github

"""
This script will collect metadata from REPOS to be
used in filters.

Metadata needed:
    - full_name
    - description
    - languages_url
    - clone_url
    - size
    - stargazers_count
    - language
    - topics

HOW TO RUN -> python3 metadata_collect.py `cat <slug txt>`
OTHERWISE  -> python3 metadata_collect.py
(latter will use the default file path below)
"""

# NOTE: METADATA LIST BELOW
METADATA = ['full_name', 'description', 'languages_url',
            'clone_url', 'size', 'stargazers_count',
            'language', 'topics']

# NOTE: Path variables.
REPO_PATH = 'textfiles/repo_names'
METADATA_PATH = 'METADATA/'

# IMPORTANT: Needed to avoid miserable rate limits on GitHub.
TOKENS = os.getenv('GITHUB_API_TOKENS', default=None)
g = scraper.GitHubAPI(TOKENS)
g2 = Github(TOKENS)


# Gets metadata for the given repo, then writes it to a file.
def get_metadata(repo_slug, dest_file) -> None:
    fptr = open(dest_file, 'w')
    data = g.repo_info(str(repo_slug))

    for kw in METADATA:
        fptr.write(kw + ':')
        fptr.write(str(data[kw]) + '\n')

    fptr.close()


# TY theresa ;)
def rate_limit_pause():
    try:
        rate_limit = g2.get_rate_limit()
    except:
        time.sleep(1)
        rate_limit = g2.get_rate_limit()

    rate = rate_limit.search
    if rate.remaining <= 1:
        print(f'Rate limit exceeded.  Reset time: {rate.reset}')
        while rate.remaining == 0:
            rate_limit = g2.get_rate_limit()
            rate = rate_limit.search
            time.sleep(1)


# Check if a file is in the directory
def in_dir(query, dir_path):
    query = query.replace('/', '_') + '.txt'
    # Loop through each file in the
    for filename in os.listdir(dir_path):
        if query == filename:
            return True

    return False


# Main function.
def _main():
    # If no additional arguments are passed into the
    # argument vector:
    if len(sys.argv) <= 1:
        print(f'Using file {REPO_PATH} to collect metadata:')

        # NOTE: Collect all slugs:
        curr_file = open(REPO_PATH, 'r')

        # NOTE: Go through each slug in the repo_names file:
        for i, filename in enumerate(curr_file.readlines()):
            filename = filename.strip()
            print(f'{i}: {filename}')
            if not in_dir(filename, 'METADATA'):
                dest = METADATA_PATH + filename.replace('/', '_') + '.txt'
                rate_limit_pause()
                get_metadata(filename, dest)

    # If the argument vector contains additional arguments:
    else:
        print('Using argument vector to collect metadata:')

        # NOTE: Go through each slug in the argument vector:
        for i, filename in enumerate(sys.argv[1:]):
            filename = filename.strip()
            print(f'{i}: {filename}')
            if not in_dir(filename, 'METADATA'):
                dest = METADATA_PATH + filename.replace('/', '_') + '.txt'
                rate_limit_pause()
                get_metadata(filename, dest)


# Run the script directly:
if __name__ == '__main__':
    _main()
