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


# Main Function:
def _main():

    # If there are no arguments passed, read from file.
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

    # r = requests.get('https://api.github.com/repos/stellargraph/stellargraph/languages')
    # fptr = open('data.json', 'w')
    # fptr.write(r.text)
    # fptr.close()
    #
    # # Opening JSON file
    # with open('data.json') as json_file:
    #     data = json.load(json_file)
    #
    # print(data['Python'])


# Run script directly:
if __name__ == '__main__':
    _main()
