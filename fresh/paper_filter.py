# Justin Ventura | Carnegie Mellon University

import sys
import json
import requests
import subprocess

"""
This script removes papers, research demos, and other
code-less candidates.

Need to collect metadata for languages:
    - First filter out Jupyter NoteBooks / No Languages
    - Then check ratio of README...
    
    
candidates -> candidates2.

-Justin Ventura
"""

# NOTE: PATH VARIABLES.
REPO_PATH = 'textfiles/CANDIDATES/candidates'
CANDS_PATH = 'textfiles/CANDIDATES/'
TRASH_PATH = 'textfiles/TRASH/'
REPO_PATH_TEST = 'test_pool'


# Check if repo has been classified yet:
def classified(full_name: str) -> bool:
    return _cands(full_name) or _trash(full_name)


# Sub method for checking the CANDIDATES tree.
def _cands(full_name: str) -> bool:
    # Search in the file for the given repo:
    search_cmd = ['grep', '-soi'] + [full_name] + [f'{CANDS_PATH}/candidates2']

    # If there is no exception, then there was at least one result.
    try:
        subprocess.check_output(tuple(search_cmd), text=True)
        return True
    except subprocess.CalledProcessError:
        return False


# Sub method for checking the TRASH tree.
def _trash(full_name: str) -> bool:
    # Search in the file for the given repo:
    search_cmd = ['grep', '-soi'] + [full_name] + [f'{TRASH_PATH}/trash2']

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


# Filter for repo languages:
def lang_filter(language: str) -> bool:
    bad_langs = ['none', 'jupyter notebook', 'tex']
    return True if language in bad_langs else False


# Check code ratios:
def code_size_filter(languages_url: str, mod_repo_name: str) -> bool:
    r = requests.get(languages_url)

    # Open the language json file:
    with open('LANG_TEMP/data.json', 'w') as json_file:
        json_file.write(r.text)

    # Load the language json to dict:
    with open('LANG_TEMP/data.json', 'r') as json_file:
        data = json.load(json_file)

    # Command to count bytes in readme:
    byte_cnt_cmd = tuple([f'<READMES/{mod_repo_name}.md', 'wc', '-c'])
    code_size = sum(data.values())
    readme_size = subprocess.check_output(byte_cnt_cmd, text=True)
    ratio = readme_size / code_size

    return True if ratio >= 0.5 else False


# Main Function:
def _main():

    # If there are no arguments passed, read from file.
    if len(sys.argv) <= 1:
        print(f'Using file {REPO_PATH_TEST} to filter:')

        # NOTE: Collect all slugs:
        curr_file = open(REPO_PATH_TEST, 'r')

        # Destination files:
        # file_cands = open('textfiles/CANDIDATES/candidates2', 'a')
        # file_trash = open('textfiles/TRASH/trash2', 'a')
        file_cands = open('test_cands', 'a')
        file_trash = open('test_trash', 'a')

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
                        if lang_filter(details['language']):
                            file_trash.write(filename)

                        # Check for the size of the code base vs README.
                        elif code_size_filter(details['languages_url'], mod_repo_name):
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
        # except:
        #     print('Process terminated unexpectedly, unknown reason.')

        # Make sure the file was written to:
        finally:
            file_cands.close()
            file_trash.close()

        # me good programmer
        file_cands.close()
        file_trash.close()


# Run script directly:
if __name__ == '__main__':
    _main()
