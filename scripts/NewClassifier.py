# Justin Ventura | Carnegie Mellon University

from RepositoryInfo import RepositoryInfo as Repo
from RepositoryInfo import DEFAULT
import requests
import re

"""
This is a new version of the classifier.  This one will
try to do more filtering and less reinforcement.
"""

# NOTE: Here are the newly formed keyword lists:
BAD_DESCRIPTION = ['api', 'framework', 'toolkit', 'tool', 'library', 'package',
                   'tutorial', 'homework', 'course', 'platform', 'examples',
                   'prototype', 'deprecated', 'interview']
BAD_TOPICS = ['api', 'framework', 'toolkit', 'tool', 'library', 'package',
              'tutorial', 'homework', 'course', 'platform', 'examples',
              'prototype', 'interview-practice', 'interview-questions',
              'interview']
TOPICS = ['machine-learning', 'artificial-intelligence', 'deep-learning',
          'neural-networks', 'ai', 'neural-nets', 'deep-neural-networks']
KEYWORDS = ['machine learning', 'artificial intelligence', 'deep learning',
            'ml', 'ai']
BAD_KEYWORDS = ['research papers',
                '<code>']


class AlphaClassifier:

    # Initialize the classifier.
    def __init__(self):
        self.score = DEFAULT      # Current score for repo.
        self._num_classified = 0  # Total num ranked.
        self._num_negated = 0     # Negate miserable scores.
        self._is_mlai = False

    def classify(self, repo: Repo, verbose: bool = False) -> None:
        """This will classify the given Repo.

        :param repo: RepositoryInfo class dubbed Repo.
        :param verbose: Verbosity for debugging.
        :return: None, modifies repo.
        """
        print('-' * 50)
        print(f'{repo.info()[2]}')
        info = repo.info()

        if verbose:
            print(info[0])
        self._scrape_desc(desc=info[0])

        if verbose:
            print(info[2])
        self._scrape_readme(full_name=info[2])

        if verbose:
            print(info[3])
        self._scrape_topics(topics=info[3])

        if verbose:
            print(info[5])
        self._check_lang(lang=info[5])

        if self._is_mlai is False:
            self.score -= 5

        # Now apply the score acquired.
        self._apply_score(repo=repo)

        # Prepare for next classification.
        self._num_classified += 1
        self._num_negated += 1 if self.score < 0 else 0
        self.score = DEFAULT
        self._is_mlai = False

    # Sub-method for scoring based on description:
    def _scrape_desc(self, desc=None) -> None:
        if desc is None:
            self.score -= 2
        else:
            if any(kw in desc for kw in BAD_DESCRIPTION):
                print('-6 found BAD KEYWORD in desc')
                self.score -= 6

    # Sub-method for scoring based on README.
    def _scrape_readme(self, full_name) -> None:
        assert(full_name is not None), 'No full_name provided.'

        r = requests.get(f'https://github.com/{full_name}/blob/master/README.md')
        for kw in KEYWORDS:
            if self._in_readme(kw=kw, readme=r.text):
                self._is_mlai = True
                break
        for kw in BAD_KEYWORDS:
            if self._in_readme(kw=kw, readme=r.text):
                self.score -= 2
        del r

    # Sub-method for regex in README to find bad keywords.
    @staticmethod
    def _in_readme(kw: str, readme: str) -> bool:
        p = re.compile(f' ({kw})', re.IGNORECASE)
        return True if p.search(readme) else False

    # Sub-method for scoring based on topics.
    def _scrape_topics(self, topics) -> None:
        if any(kw in topics for kw in BAD_TOPICS):
            self.score -= 2

        if any(kw in topics for kw in TOPICS):
            self._is_mlai = True

    # Sub-method for scoring based on language.
    def _check_lang(self, lang) -> None:
        if lang is None:
            print('-10 no language')
            self.score -= 10
        else:
            self.score -= 4 if lang == 'jupyter notebook' else 0
            if lang == 'jupyter notebook':
                print('-4 for jupyter notebook')

    # Sub-method for giving a score to the repo.
    def _apply_score(self, repo: Repo) -> None:
        print(f'FINAL SCORE: {self.score}')
        repo.apply_rank(self.score)
