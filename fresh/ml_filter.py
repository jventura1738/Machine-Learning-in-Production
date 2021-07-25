# Justin Ventura | Carnegie Mellon University

import os
import sys
import time
import github
import subprocess
from code_filter import clone_repo, check_code, delete_repo

"""
This file filters out repos which do not contain some sort of
machine learning aspect.

Heuristics:
X
Y
Z
"""

# NOTE: Path variables
README_PATH = os.getcwd() + '/READMES/'
REPO_PATH = 'textfiles/repo_names'
REPO_PATH2 = 'textfiles/repo_names2'
CANDS_PATH = 'textfiles/CANDIDATES/'
TRASH_PATH = 'textfiles/TRASH/'

# NOTE: Keyword lists:
KEYWORDS = ['machine learning', 'artificial intelligence',
            'deep learning', 'neural net', 'classifier']
TOPICS = ['machine-learning', 'artificial-intelligence',
          'deeplearning', 'deep-learning',
          'machinelearning', 'neural-networks',
          'neural-network', 'classifier', 'classification']
FILE_DIR_QUERIES = ['model', 'models', 'model.*', 'classify', 
                    'classify.*', 'train.*', 'datasets', 'train',
                    'training']
QUERIES = ['sklearn', 'keras', 'tensorflow', 'torch']


# Check if repo has been classified yet:
def classified(full_name: str) -> bool:
    return _cands(full_name) or _trash(full_name)


# Sub method for checking the CANDIDATES tree.
def _cands(full_name: str) -> bool:
    # Search in the file for the given repo:
    search_cmd = ['grep', '-soi'] + [full_name] + [f'{CANDS_PATH}/candidates']

    # If there is no exception, then there was at least one result.
    try:
        subprocess.check_output(tuple(search_cmd), text=True)
        return True
    except subprocess.CalledProcessError:
        return False


# Sub method for checking the TRASH tree.
def _trash(full_name: str) -> bool:
    # Search in the file for the given repo:
    search_cmd = ['grep', '-soi'] + [full_name] + [f'{TRASH_PATH}/trash']

    # If there is no exception, then there was at least one result.
    try:
        subprocess.check_output(tuple(search_cmd), text=True)
        return True
    except subprocess.CalledProcessError:
        return False


# Get metadata from a repo given its modified repo name,
# in the format owner_reponame.txt.
def metadata(mod_repo_name: str):
    # Prepare dictionary for metadata:
    fptr = open(f'METADATA/{mod_repo_name}', 'r')
    meta = dict()

    # Assume specific format (guaranteed by my script):
    for line in fptr.readlines():
        k, v = tuple(line.split(':', 1))
        meta[k] = v.strip()

    # Returns dictionary, be wary of defective files.
    return meta


# This function goes through the description searching for
# keywords indicative of ML/AI.
# TRUE: passes filter.
# FALSE: fails filter.
def desc_filter(desc: str) -> bool:
    # If no description, move on.
    if desc is None:
        return False

    # Otherwise, check description for keywords:
    else:
        return True if any(kw in desc for kw in KEYWORDS) else False


# This function goes through topics looking for words
# indicative of ML/AI.
# TRUE: passes filter.
# FALSE: fails filter.
def topic_filter(topics: str) -> bool:
    # If no topics, move on.
    if topics is None or len(topics) == 0:
        return False

    # Otherwise, check topics list:
    else:
        return True if any(kw in topics for kw in TOPICS) else False


# This function goes through READMEs to search for
# sign of machine learning.
# TRUE: passes filter.
# FALSE: fails filter.
def readme_filter(mod_repo_name: str) -> bool:
    # Look for README (if there is one):
    try:
        # Check README.txt file for keywords:
        fptr = open(README_PATH + f'{mod_repo_name + ".md"}', 'r')
        return True if any(kw in fptr.read() for kw in KEYWORDS) else False

    # If no README, just move on.
    except FileNotFoundError:
        print(f'{mod_repo_name}.md does not exist.')
        return True


# Check the repository for filenames or directory names which
# could be indicative of ML/AI.
def repo_filename_filter(dir_name: str):
    repo_name = dir_name.split('/')[-1]
    # Loop through the queries:
    for query in FILE_DIR_QUERIES:
        # Commands to find file/dir names matching query:
        find_cmd = ['find', '-L', f'{repo_name}', '-iname'] + [query]
        cnt_cmd = ['wc', '-l']

        try:
            # Pipe results from find to wc to find occurences:
            out = subprocess.check_output(tuple(find_cmd), text=True)
            res = subprocess.check_output(tuple(cnt_cmd), input=out, text=True)

            if int(res.strip()) >= 1:
                return True
        except subprocess.CalledProcessError:
            return False

    return False


# IMPORTANT: If all above fails, check through each file in the repo
# IMPORTANT: code to see if there are signs of a ML model.
def repo_code_filter(full_name: str, clone_url: str) -> bool:
    # Clone the repository locally:
    if clone_repo(full_name=full_name, clone_url=clone_url):
        filename = full_name.split('/')[-1]

        # Check the tree nodes first:
        if repo_filename_filter(filename.strip()):
            delete_repo(full_name=full_name)
            return True

        # Otherwise:
        else:
            # Loop through and query the repo codebase:
            for q in QUERIES:
                if check_code(full_name=full_name, query=q) == True:
                    delete_repo(full_name=full_name)
                    return True

            # If no words found the code, return False.
            delete_repo(full_name=full_name)
            return False
    else:
        print('Clone failed :(')
        delete_repo(full_name=full_name)
        time.sleep(10)


# Main function:
def _main():

    # If no additional arguments are passed into the
    # argument vector:
    if len(sys.argv) <= 1:
        print(f'Using file {REPO_PATH} to filter:')

        # NOTE: Collect all slugs:
        curr_file = open(REPO_PATH, 'r')

        # Destination files:
        file_cands = open('textfiles/CANDIDATES/candidates', 'a')
        file_trash = open('textfiles/TRASH/trash', 'a')

        try:

            # NOTE: Go through each slug in the repo_names file:
            for filename in curr_file.readlines():
                # Initial path here; will be added on to later:
                mod_repo_name = (filename.strip()).replace('/', '_')

                # Only go through this process if the repository has not
                # already gone through the filter.
                if not classified(filename.strip()):
                    print(f'classifying {filename.strip()}')
                    details = metadata(mod_repo_name + '.txt')

                    # If there is no metadata:
                    if len(details) != 8:
                        print(f'{filename.strip()} has no metadata.')
                        file_trash.write(filename)

                    # Otherwise:
                    else:
                        # Filter based on repository description:
                        if desc_filter(details['description']):
                            file_cands.write(filename)

                        # Then check repository topics next:
                        elif topic_filter(details['topics']):
                            file_cands.write(filename)

                        # Then check README:
                        elif readme_filter(mod_repo_name):
                            file_cands.write(filename)

                        # This is the sophisticated part of the filter:
                        else:
                            # Check the filenames and directories to hopefully speed up filter.
                            flag = repo_code_filter(details['full_name'], details['clone_url'])
                        
                            if flag is False:
                                file_trash.write(filename)
                            else:
                                file_cands.write(filename)


                # Repo has already been classified.
                else:
                    print(f'{filename.strip()} already classified.')

        # Just in case it terminals to a signal:
        except KeyboardInterrupt:
            print('Process terminated unexpectedly via signal.')

        # Other issues:
        except:
            print('Process terminated unexpectedly, unknown reason.')
        
        # Make sure the file was written to:
        finally:
            file_cands.close()
            file_trash.close()
    
        # me good programmer
        file_cands.close()
        file_trash.close()

    # TODO: UPDATE THIS PART TO USE ARGV:
    # If the argument vector contains additional arguments:
    else:
        print('Using argument vector to filter:')

        # NOTE: Go through each slug in the argument vector:
        for filename in sys.argv[1:]:

            # Initial path here; will be added on to later:
            dest_path = f'textfiles/{filename}'

            # TODO: Here we will run the filters.
            try:
                # First, make sure the repo is actually some sort
                # of project and not a paper or list.
                dest_path += ''

            except github.GithubException as g_err:
                if g_err.status == 404:
                    print('README not found, moving on.')
                elif g_err.status == 403:
                    print('Rate Limit Exceeded (GitHub)')
                    print('5000 req/hr max.')
                    exit(1)


# Run script directly:
if __name__ == '__main__':
    _main()
