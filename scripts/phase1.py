# Justin Ventura | Carnegie Mellon University

# Libraries:
import os
import sys
import time
import stscraper as scraper
from RepositoryInfo import RepositoryInfo as Repo
from BetaClassifier import BetaClassifier as ClassifierV1

"""
DESCRIPTION:
This script will be used to scrape (primarily) github
for software with the criteria we need it to fit.

THE CHALLENGE: we are NOT looking for frameworks, APIs,
school projects, student work, demos for research papers
or thesis', notebook experiments, nor hackathon projects.

WHAT WE WANT: open source commercial software with some
sort of ML/AI implementation.  Simple filters will not
yield desired results, so we are still trying to figure
out an effective way to scrape.  Brute forcing is not
an option since it would require human validation which
is astronomically slow, and painful.

IDEAS:

1) possibly a scoring system to rank repos found based
   on keywords (in desc/readme), topics (if any), number
   of stars, contributors, and forks, and potentially
   check through source code for signs of ML/AI.  Maybe
   look for inclusion of libraries.  Still need to find
   a way to filter out libraries, projects, frameworks,
   etc.
"""

# IMPORTANT: Needed to avoid miserable rate limits on GitHub.
TOKENS = os.getenv('GITHUB_API_TOKENS', default=None)


# This is the first version of the search.
def search_v1(demo: bool = False) -> None:
    """This is the first attempt at finding repos.

    - First Step is to do testing -

    :return: None
    """
    # NOTE: This demo is for testing purposes:
    if demo:
        gh_api = scraper.GitHubAPI(TOKENS)
        repo_list = list()

        # Iterate the given list
        for repo_name in sys.argv[1:]:
            # NOTE: format as <username/repository_name>
            targ_info = gh_api.repo_info(str(repo_name))

            # This is where useful data is stored:
            repo_info = dict()
            repo_info['category'] = 'N/A'
            repo_info['gh_id'] = targ_info['id']
            repo_info['name'] = targ_info['name'].lower()
            repo_info['full_name'] = targ_info['full_name'].lower()
            repo_info['desc'] = targ_info['description'].lower()
            repo_info['created'] = targ_info['created_at']
            repo_info['last_update'] = targ_info['updated_at']
            repo_info['size'] = targ_info['size']
            repo_info['homepage'] = targ_info['homepage'].lower()
            repo_info['topics'] = targ_info['topics']
            repo_info['forks'] = targ_info['forks']
            repo_info['stars'] = targ_info['stargazers_count']
            repo_info['license'] = targ_info['license']
            repo_info['language'] = targ_info['language'].lower()

            repo_list.append(Repo(repo_info=repo_info))

        Lambda = ClassifierV1()
        for repo in repo_list:
            Lambda.classify(repo, verbose=False)
            print(f'{repo.full_info()["full_name"]}: {repo.ranking()}')
            print('-'*30)

    # NOTE: This is for the real prototype:
    else:
        pass


# TODO: perform a real search.
def _main():
    search_v1(demo=True)


# Run script directly.
if __name__ == '__main__':
    _main()
