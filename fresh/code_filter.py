# Justin Ventura | Carnegie Mellon University

import time
import subprocess

"""
This file clones a repository temporarily to do a small analysis
on the code in order to see if there is some sort of ML/AI.
"""

# Path to the metadata.
PATH_TO_METADATA = 'METADATA/'


# Clone the repository given the metadata file:
def clone_repo(full_name: str, clone_url: str) -> None:
    # Clone the given repository using the url:
    clone_cmd = ['git', 'clone'] + [clone_url]
    clone = subprocess.run(clone_cmd, text=True)

    # Log the successful and unsuccessful clones:
    if clone.returncode == 0:
        print(f'{full_name} cloned successfully.')
    else:
        print(f'{full_name} clone failed; may exist already.')
        time.sleep(3)


# Check the code for occurrences of a word:
def check_code(full_name: str, query: str) -> bool:
    # Get directory name:
    repo_name = full_name.split('/')[-1]

    # Run the command to find the query:
    search_cmd = ['grep', '-sroi'] + [query] + [repo_name]

    try:
        subprocess.check_output(tuple(search_cmd), text=True)
        return True
        # Count the number of occurrences by piping `output.`
        # output = subprocess.check_output(tuple(search_cmd), text=True)
        # counter = subprocess.run(['wc', '-l'], stdout=subprocess.PIPE, text=True, input=output)
        # count = int(counter.stdout.strip())
        # return True if count >= 1 else False
    except subprocess.CalledProcessError:
        return False


# IMPORTANT: THIS WILL COMPLETELY DELETE THE GIVEN REPOSITORY
# IMPORTANT: AND ALL OF ITS CONTENTS!
def delete_repo(full_name: str) -> None:
    # Delete the given repository:
    repo_name = full_name.split('/')[-1]
    delete_cmd = ['rm', '-rf'] + [repo_name]
    delete = subprocess.run(delete_cmd, text=True)

    # Log the successful and unsuccessful removal:
    if delete.returncode == 0:
        print(f'{full_name} removed successfully.')
    else:
        print(f'{full_name} removal failed; may not exist.')
        time.sleep(3)


# NOTE: Main function for testing:
def _main():
    # Setup for testing:
    repo_slug = 'deepfakes/faceswap'
    query = 'layers.py'
    clone_url = 'https://github.com/deepfakes/faceswap.git'

    # Perform the test:
    clone_repo(full_name=repo_slug, clone_url=clone_url)
    if check_code(full_name=repo_slug, query=query):
        print(f'Found {query}!')
        time.sleep(3)
    else:
        print(f'{query} not found.')
        time.sleep(3)
    delete_repo(full_name=repo_slug)


# Run script directly:
if __name__ == '__main__':
    _main()
