# Justin Ventura | Carnegie Mellon University

import os
import sys
from github import Github

"""
THIS IS A TESTING SCRIPT, WILL BE USELESS LATER.

-Justin Ventura
"""

# IMPORTANT: Needed to avoid miserable rate limits on GitHub.
TOKENS = os.getenv('GITHUB_API_TOKENS', default=None)
g = Github(TOKENS)


# Function to search on Github
def search_github(kw):
    query = '+'.join(kw) + '+in:readme+in:description'
    result = g.search_repositories(query, 'stars', 'desc')
    return result

# Main function:
def _main():
    keywords = sys.argv[1:]
    results = search_github(keywords)
    for repo in results:
        print(f'{repo.full_name}, {repo.stargazers_count} stars')


# Directly run the script for action:
if __name__ == '__main__':
    _main()
