# Justin Ventura | Carnegie Mellon University

# Libraries:
import os
import sys
import csv
import stscraper as scraper

# IMPORTANT: CONSTANTS
TOKENS = os.getenv('GITHUB_API_TOKENS', default=None)
FIELDS = ['category', 'gh_id', 'name', 'full_name', #'owner',
          'desc', 'created', 'last_update', 'size', 'forks',
          'stars', 'language']

"""
Short script for direct access to GitHub repos via
the GitHub API.

HOW TO RUN:
> python3 direct.py `cat repo_names`
"""


def write_to_csv(data_list):
    csv_file = "repo_data.csv"
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=FIELDS)
            writer.writeheader()
            for data in data_list:
                writer.writerow(data)
    except IOError:
        print('IO Error.')


# Main script:
# noinspection PyUnresolvedReferences
def _main():
    # This is the API object which will be interacted with.
    # NOTE: this is for GitHubAPIv3 currently.
    gh_api = scraper.GitHubAPI(TOKENS)

    data_list = list()

    # Iterate over the commandline arguments:
    for repo_name in sys.argv[1:]:

        # NOTE: format as <username/repository_name>
        targ_slug = str(repo_name)

        # Scrape and store here:
        targ_info = gh_api.repo_info(targ_slug)

        # This is where useful data is stored:
        df_data = dict()

        # TODO: figure out the commented sections below.
        df_data['category'] = 'N/A'
        df_data['gh_id'] = targ_info['id']
        df_data['name'] = targ_info['name']
        df_data['full_name'] = targ_info['full_name']
        # df_data['owner'] = targ_info['owner']
        df_data['desc'] = targ_info['description']
        df_data['created'] = targ_info['created_at']
        # df_data['last_commit'] = targ_info['updated_at']
        df_data['last_update'] = targ_info['updated_at']
        df_data['size'] = targ_info['size']
        df_data['forks'] = targ_info['forks']
        df_data['stars'] = targ_info['stargazers_count']
        # df_data['contributors'] = targ_info['name']
        df_data['language'] = targ_info['language']
        data_list.append(df_data)

    write_to_csv(data_list)


# Ensure directly running the script; not a module.
if __name__ == '__main__':
    _main()
