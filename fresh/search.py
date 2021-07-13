# Justin Ventura | Carnegie Mellon University

import os
import sys
from github import Github

"""
PHASE 1: SEARCH.

This script is for searching for repositories by keyword,
then puts their slugs into a repo list.

HOW TO RUN -> python3 search.py `cat keywords`
then do    -> sort repo_list | uniq -u > repo_names

-Justin Ventura
"""

# NOTE: This is the path to the keyword text file.
PATH = 'textfiles/repo_list'


# IMPORTANT: Needed to avoid miserable rate limits on GitHub.
TOKENS = os.getenv('GITHUB_API_TOKENS', default=None)
g = Github(TOKENS)


# Function to search on Github
def search_github(kw):

    # Check the GitHub API rate limit:
    rate_limit = g.get_rate_limit()
    rate = rate_limit.search
    if rate.remaining == 0:
        print(f'You have 0/{rate.limit} API calls remaining. Reset time: {rate.reset}')
        return
    else:
        print(f'You have {rate.remaining}/{rate.limit} API calls remaining')

    # Perform the search using the keywords:
    # query = '+'.join(kw) + '+in:readme in:description stars:>=100 pushed:>2021-01-01'
    query = kw + 'stars:>=100 pushed:>2021-01-01'
    result = g.search_repositories(query, 'stars', 'desc')

    # Return the resulting Paginated List
    return result


# Check if a repo is in the given file.
def in_file(filename: str, repo_slug: str) -> bool:
    with open(filename) as f:
        if repo_slug in f.read():
            return True
    return False


# Main function:
def _main():
    # Get keywords from the command line:
    keywords = sys.argv[1:]

    # Use keywords to find repositories.
    results = list()
    for kw in keywords:
        try:
            results += search_github(kw)
        except:
            print('Rate Limit Reached.')
            break

    # Write repository slugs to a file.
    fptr = open(PATH, 'a')
    for repo in results:
        if not in_file(filename=PATH, repo_slug=repo.full_name):
            fptr.write(repo.full_name + '\n')


# Directly run the script for action:
if __name__ == '__main__':
    _main()
