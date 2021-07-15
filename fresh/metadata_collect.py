# Justin Ventura | Carnegie Mellon University

import os
import sys
import stscraper as scraper

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


# Gets metadata for the given repo, then writes it to a file.
def get_metadata(repo_slug, dest_file) -> None:
    fptr = open(dest_file, 'w')
    data = g.repo_info(repo_slug=repo_slug)

    for kw in METADATA:
        fptr.write(data[kw] + '\n')

    fptr.close()


# Main function.
def _main():
    # If no additional arguments are passed into the
    # argument vector:
    if len(sys.argv) <= 1:
        print(f'Using file {REPO_PATH} to collect metadata:')

        # NOTE: Collect all slugs:
        curr_file = open(REPO_PATH, 'r')

        # NOTE: Go through each slug in the repo_names file:
        for filename in curr_file.readlines():
            dest = METADATA_PATH + filename.replace('/', '_') + '.txt'
            get_metadata(filename, dest)

    # If the argument vector contains additional arguments:
    else:
        print('Using argument vector to collect metadata:')

        # NOTE: Go through each slug in the argument vector:
        for filename in sys.argv[1:]:
            dest = METADATA_PATH + filename.replace('/', '_') + '.txt'
            get_metadata(filename, dest)


# Run the script directly:
if __name__ == '__main__':
    _main()
