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
        self.score = 10    # Default is 10, may change.
        self.label = None  # Decided by classifier.
        self._info = repo_info

    # Returns tuple of this repo's ranking.
    def ranking(self) -> Tuple[int, str]:
        return self.score, self.label

    # Get the repository information.
    def info(self) -> Dict:
        return self._info

    # Gets the full name, for storing purposes.
    def __str__(self) -> str:
        return self._info['full_name'] if self._info is not None else None
