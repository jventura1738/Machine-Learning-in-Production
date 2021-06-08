# Justin Ventura | Carnegie Mellon University

from RepositoryInfo import RepositoryInfo as Repo

"""
This is a prototype classifier to begin some
preliminary testing.  This will evolve over
time.

PLAN OF CLASSIFICATION:
    1) give a score based on criteria (adjust as needed)
    2) classify as such:
        a) negative score -> 'REJECT'
        b) score btwn 1-6 -> 'WARNING'
        c) score btwn 7-9 -> 'UNSURE'
        d) score exact 10 -> 'CHECK'
        e) score above 10 -> 'LIKELY'

- Justin Ventura
"""


# Classifier class:
class BetaClassifier:

    # Initialize the classifier.
    def __init__(self):
        self._num_classified = 0   # Total num ranked.
        self._num_negated = 0      # Negate miserable scores.

    # IMPORTANT: THIS IS THE CLASSIFICATION 'ALGORITHM'
    def classify(self, repo: Repo) -> None:
        pass
