# Justin Ventura | Carnegie Mellon University

import os
import re
import sys
import requests
from github import Github

"""
This file is for extracting and grouping code snippets from
candidate repositories.
"""

FENCED_CODE = re.compile(
    r"```[a-z]*\n[\s\S]*?\n*```"
)

# FENCED_CODE = re.compile(
#     r'( {0,3})(`{3,}|~{3,})([^`\n]*)\n'
#     r'(?:|([\s\S]*?)\n)'
#     r'(?: {0,3}\2[~`]* *\n+|$)'
# )

PATH = 'readme_processing/results.md'

# IMPORTANT: Needed to avoid miserable rate limits on GitHub.
TOKENS = os.getenv('GITHUB_API_TOKENS', default=None)
g = Github(TOKENS)


# Extracts snippets and puts them into a file.
def snippet_extraction(repo_slug, dest) -> None:
    assert (repo_slug is not None), 'No full_name provided.'

    # Get the readme raw...
    readme_url = g.get_repo(repo_slug).get_readme().download_url
    r = requests.get(readme_url)

    # Search for the pattern in the raw markdown:
    code_blocks = FENCED_CODE.findall(r.text)

    # Write the beginning section (for code blocks).
    dest.write(f'# {repo_slug}, {len(code_blocks)} blocks.' + '\n\n')
    for code in code_blocks:
        dest.write(code+'\n\n')


# NOTE: format for elem in argv should be user/repo_name.
def _main():
    repos = sys.argv[1:]
    fptr = open(f'{PATH}', 'a')
    for repo in repos:
        snippet_extraction(repo_slug=repo, dest=fptr)


# Run the script directly for anything to happen.
if __name__ == '__main__':
    _main()
