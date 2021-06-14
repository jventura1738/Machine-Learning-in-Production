# Justin Ventura | Carnegie Mellon University

import os
import sys
import time
import datetime
from github import Github

"""
THIS IS A TESTING SCRIPT, WILL BE USELESS LATER.

-Justin Ventura
"""

# NOTE: TEST QUERIES:
# query = 'a' + 'in:name'
# query = '+'.join(kw) + '+in:readme+in:description'

# IMPORTANT: Needed to avoid miserable rate limits on GitHub.
TOKENS = os.getenv('GITHUB_API_TOKENS', default=None)
g = Github(TOKENS)

# Cutoff date for filter:
CUTOFF = datetime.datetime(2021, 1, 1)

# Function to search on Github
def search_github(kw):
    rate_limit = g.get_rate_limit()
    rate = rate_limit.search
    if rate.remaining == 0:
        print(f'You have 0/{rate.limit} API calls remaining. Reset time: {rate.reset}')
        return
    else:
        print(f'You have {rate.remaining}/{rate.limit} API calls remaining')
    # query = '+'.join(kw)+'in:name+stars:>=100'
    query = '+'.join(kw) + '+in:readme in:description stars:>=100 pushed:>2021-01-01'
    result = g.search_repositories(query, 'stars', 'desc')
    return result

# Main function:
def _main():
    # keywords = sys.argv[1:]
    keywords = 'machine learning'
    results = search_github(keywords)
    fptr = open('repo_names2', 'w')
    for i, repo in enumerate(results):
        if repo.pushed_at <= CUTOFF:
            i -= 1
            continue
        fptr.write(repo.full_name+'\n')
        if i == 500:
            break


# Directly run the script for action:
if __name__ == '__main__':
    _main()
