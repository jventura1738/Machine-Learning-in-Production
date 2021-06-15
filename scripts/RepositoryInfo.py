# Justin Ventura | Carnegie Mellon University

from typing import Tuple, Dict

"""
This class contains the repository info including
the class in which the Classifier considers it
to be in.
"""

DEFAULT = 0

# RepositoryInfo class for high level interaction:
class RepositoryInfo:

    # Initialize the repository:
    def __init__(self, repo_info: Dict = None):
        self._score = DEFAULT    # Default may change.
        self._info = repo_info

    # NOTE: This returns the actual info I care about in
    # NOTE: the classification algorithm.
    def info(self):
        return [
            self._info['desc'],       # Used to search keywords.
            self._info['homepage'],  # Check if homepage.
            self._info['full_name'],  # Used to scrape README.
            self._info['topics'],     # Same as above desc.
            self._info['license'],    # Experimental.
            self._info['language'],   # Experimental.
        ]

    # Apply ranking to the repository:
    def apply_rank(self, score=10):
        self._score = score

    # Returns tuple of this repo's ranking.
    def ranking(self) -> int:
        return self._score

    # Get the full repository information.
    def full_info(self) -> Dict:
        return self._info

    # Gets the full name, for storing purposes.
    def __str__(self) -> str:
        return self._info['full_name'] if self._info is not None else None
