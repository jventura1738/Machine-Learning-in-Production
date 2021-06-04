# Justin Ventura | Carnegie Mellon University

# Libraries:
import os
import numpy as np
import pandas as pd
import stscraper as scraper

TOKENS = os.getenv('GITHUB_API_TOKENS', default=None)

"""
Short script for direct access to GitHub repos via
the GitHub API.
"""

# Main script:
def _main():
    gh_api = scraper.GitHubAPI(TOKENS)
    targ_slug = input('Enter target repo name: ')
    mid = targ_slug.index('/')
    fp = open(f'{targ_slug[mid+1:]}.txt', 'w')
    targ_info = gh_api.repo_info(targ_slug)
    for k, v in targ_info.items():
        fp.write(f'{k}: {v}\n')
    fp.close()

# Ensure directly running the script; not a module.
if __name__ == '__main__':
    _main()
