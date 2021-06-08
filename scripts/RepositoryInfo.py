# Justin Ventura | Carnegie Mellon University

from typing import Tuple, Dict

"""
This class contains the repository info including
the class in which the Classifier considers it
to be in.
"""


# RepositoryInfo class for high level interaction:
class RepositoryInfo:

    # Initialize the repository:
    def __init__(self, repo_info: Dict = None):
        self._score = 10    # Default is 10, may change.
        self._label = None  # Decided by classifier.
        self._info = repo_info

    # NOTE: This returns the actual info I care about in
    # NOTE: the classification algorithm.
    def info(self):
        return [
            self._info['full_name'],  # Used to scrape README.
            self._info['desc'],       # Used to search keywords.
            self._info['topics'],     # Same as above.
            self._info['license'],    # Experimental.
        ]

    # Apply ranking to the repository:
    def apply_rank(self, score=10, label='CHECK'):
        self._score = score
        self._label = label

    # Returns tuple of this repo's ranking.
    def ranking(self) -> Tuple[int, str]:
        return self._score, self._label

    # Get the full repository information.
    def full_info(self) -> Dict:
        return self._info

    # Gets the full name, for storing purposes.
    def __str__(self) -> str:
        return self._info['full_name'] if self._info is not None else None
