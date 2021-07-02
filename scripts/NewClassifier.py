# Justin Ventura | Carnegie Mellon University

from RepositoryInfo import RepositoryInfo as Repo
from RepositoryInfo import DEFAULT
import requests
import re

"""
This is the newest version of the classifier, where it will
filter out useless stuff, then pay closer attention to the
other details besides key words.
"""

# NOTE: Here are the newly formed keyword lists:
BAD_DESCRIPTION = ['api', 'framework', 'toolkit', 'tool', 'library', 'package',
                   'tutorial', 'homework', 'course', 'platform', 'examples',
                   'prototype', 'deprecated', 'interview', 'engine']
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
LANGUAGES = ['jupyter notebook', 'matlab', 'tex']


class NewClassifier:

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
        if self._in_name(info[2]):
            self.score -= 5

        # if verbose:
        #     print(info[2])
        # self._scrape_readme(full_name=info[2])

        if verbose:
            print(info[3])
        self._scrape_topics(topics=info[3])

        if verbose:
            print(info[5])
        self._check_lang(lang=info[5])

        if self._is_mlai is False:
            self.score -= 2

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
                print('-1 found BAD KEYWORD in desc')
                self.score -= 1

    # Sub-method for name-based filtering.
    def _in_name(self, full_name) -> bool:
        p = re.compile(f'{"awesome"}', re.IGNORECASE)
        return True if p.search(full_name) else False

    # Sub-method for scoring based on README.
    def _scrape_readme(self, full_name) -> None:
        assert(full_name is not None), 'No full_name provided.'

        r = requests.get(f'https://raw.githubusercontent.com/{full_name}/master/readme.md')
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
            print('-5 no language')
            self.score -= 5
        else:
            self.score -= 2 if lang in LANGUAGES else 0
            if lang == 'jupyter notebook':
                print('-2 for jupyter notebook')

    # Sub-method for giving a score to the repo.
    def _apply_score(self, repo: Repo) -> None:
        print(f'FINAL SCORE: {self.score}')
        repo.apply_rank(self.score)
