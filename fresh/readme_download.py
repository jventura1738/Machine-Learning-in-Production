# Justin Ventura | Carnegie Mellon University

import os
import sys
import time

import github
import requests
from github import Github

"""
This file is for downloading READMEs of each file
passed into the argument vector.
"""


# IMPORTANT: Needed to avoid miserable rate limits on GitHub.
TOKENS = os.getenv('GITHUB_API_TOKENS', default=None)
g = Github(TOKENS)


# Check if a query is in a directory:
def in_dir(dir, query) -> bool:
    return os.path.exists(f'{dir}/{query}.md')


# Function to download and write the README.
def download_readme(repo_slug) -> None:
    assert (repo_slug is not None), 'No repo_slug provided.'

    # File friendly reformat:
    temp = repo_slug.replace("/", "_")

    if not in_dir('READMES', temp):
        # Get the readme raw...
        print(repo_slug)
        try:
            readme_url = g.get_repo(repo_slug).get_readme().download_url
            r = requests.get(readme_url)
            # Write the README to the file:
            fptr = open(f'READMES/{temp}.md', 'w')
            fptr.write(r.text)
            fptr.close()
        except github.GithubException as g_err:
            if g_err.status == 404:
                print('README not found, moving on.')
            elif g_err.status == 403:
                print('Rate Limit Exceeded (GitHub)')
                print('5000 req/hr max.')
                exit(1)


# Main function.
def _main():
    repos = sys.argv[1:]
    for i, repo in enumerate(repos):
        download_readme(repo)
        print(i)


# Run the script directly.
if __name__ == '__main__':
    _main()