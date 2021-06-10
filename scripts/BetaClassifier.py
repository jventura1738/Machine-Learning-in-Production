# Justin Ventura | Carnegie Mellon University

import re
import sys
import time
import stscraper as scraper
from RepositoryInfo import RepositoryInfo as Repo
from RepositoryInfo import DEFAULT

import requests

"""
This is a prototype classifier to begin some
preliminary testing.  This will evolve over
time.

PLAN OF CLASSIFICATION:
    1) give a score based on criteria (adjust as needed)

    2) Explanations as of now:
        a) DESCRIPTION:
            - If there is none, subtract 3 points. This
              seems not to be software from experience.
            - If the description contains a word in the
              list [API, framework, toolkit, tool, lib
              library, platform, project, course], then
              subtract points off.  From my experience,
              these are huge red flags.
            - If the description has any words in the
              list [software, system, application] then
              add some points.
        b) HOMEPAGE: If there is a home page, add a few
           points as this is typically indicative of
           being some sort of software system, usually
           a web app.
        c) README:
            - If any of the above words from the first
              list are found, take away points, but not
              as many.
        d) TOPICS:
            - If one of the topics is in the following
              list [API, framework, library, toolkit,
              tool] then take off points.
        e) LICENSE (experimental):
            - If there is no license, take off a point.
        f) LANGUAGE (experimental):
            - If Jupyter Notebook > 50%, take off 4 pts.

    3) classify as such:
        a) negative score -> 'REJECT'
        b) score btwn 1-6 -> 'WARNING'
        c) score btwn 7-9 -> 'UNSURE'
        d) score exact 10 -> 'CHECK'
        e) score above 10 -> 'LIKELY'

- Justin Ventura
"""

# NOTE: Keyword lists for regex.
BAD_KEYWORDS = ['api', 'framework', 'toolkit', 'tool', 'lib',
                'library', 'platform', 'project', 'course',
                'examples', 'guideline', 'guidelines',
                'tutorial', 'package', 'learn', 'deprecated']
BAD_KEYWORDS2 = ['api', 'framework', 'library', 'toolkit',
                 'tool', 'course', 'class', 'tutorial',
                 'deprecated']
BAD_KEYWORDS3 = ['toolkit', 'framework', 'deprecated',
                 'homework', 'homeworks', 'platform',
                 'reference', 'package']
GOOD_KEYWORDS = ['software', 'system', 'application', 'service',
                 'powered by', 'app']
GOOD_KEYWORDS2 = ['machine-learning', 'artificial-intelligence',
                  'ai', 'neural-networks', 'deep-learning']
GOOD_KEYWORDS3 = ['machine learning', 'artificial intelligence',
                  'ai', 'neural networks', 'deep learning']
GOOD_KEYWORDS4 = ['download', 'production', 'software',
                  'powered by', 'machine learning',
                  'artificial intelligence', 'photos', 'photo!']

# Classifier class:
class BetaClassifier:

    # Initialize the classifier.
    def __init__(self):
        self.score = DEFAULT       # Current score for repo.
        self._num_classified = 0   # Total num ranked.
        self._num_negated = 0      # Negate miserable scores.

    # IMPORTANT: THIS IS THE CLASSIFICATION 'ALGORITHM'
    # NOTE: ENSURE KEYWORDS ARE LOWER CASED IN PREPROCESSING!
    def classify(self, repo: Repo, verbose: bool = False) -> None:
        """This will classify the given Repo.

        :param repo: RepositoryInfo class dubbed Repo.
        :param verbose: Verbosity for debugging.
        :return: None, modifies repo.
        """
        info = repo.info()

        if verbose:
            print(info[0])
        self._scrape_desc(desc=info[0])

        if verbose:
            print(info[1])
        self._check_homepage(homepage=info[1])

        if verbose:
            print(info[2])
        self._scrape_readme(full_name=info[2])

        if verbose:
            print(info[3])
        self._scrape_topics(topics=info[3])

        if verbose:
            print(info[4])
        self._check_license(lic=info[4])

        if verbose:
            print(info[5])
        self._check_lang(lang=info[5])

        # Now apply the score acquired.
        self._apply_score(repo=repo)

        # Prepare for next classification.
        self._num_classified += 1
        self._num_negated += 1 if self.score < 0 else 0
        self.score = DEFAULT

    # Sub-method for scoring based on description:
    # @staticmethod
    def _scrape_desc(self, desc=None) -> None:
        if desc is None:
            self.score -= 2
        else:
            if any(kw in desc for kw in BAD_KEYWORDS):
                self.score -= 6

            if any(kw in desc for kw in GOOD_KEYWORDS):
                self.score += 2

    # Sub-method for scoring based on homepage.
    def _check_homepage(self, homepage) -> None:
        self.score += 2 if homepage else 0

    # Sub-method for scoring based on README.
    def _scrape_readme(self, full_name) -> None:
        assert(full_name is not None), 'No full_name provided.'

        r = requests.get(f'https://github.com/{full_name}/blob/master/README.md')

        for kw in BAD_KEYWORDS3:
            if self._in_readme(kw=kw, readme=r.text):
                #print(f'{kw} found, deducting 2 points.')
                self.score -= 2
                continue

        for kw in GOOD_KEYWORDS4:
            if self._in_readme(kw=kw, readme=r.text):
                #print(f'{kw} found, adding 1 point.')
                self.score += 1
                continue

        del r

    # Sub-method for regex in README to find bad keywords.
    @staticmethod
    def _in_readme(kw: str, readme: str) -> bool:
        p = re.compile(f' ({kw})', re.IGNORECASE)
        return True if p.search(readme) else False

    # Sub-method for scoring based on topics.
    def _scrape_topics(self, topics) -> None:
        if topics is None or topics == []:
            self.score -= 3

        if any(kw in topics for kw in BAD_KEYWORDS2):
            self.score -= 5

        if all(kw not in topics for kw in GOOD_KEYWORDS2):
            self.score -= 3

    # Sub-method for scoring based on license.
    def _check_license(self, lic) -> None:
        self.score -= 0 if lic else 1

    # Sub-method for scoring based on language.
    def _check_lang(self, lang) -> None:
        if lang is None:
            self.score -= 10
        else:
            self.score -= 4 if lang == 'jupyter notebook' else 0

    # Sub-method for giving a score to the repo.
    def _apply_score(self, repo: Repo) -> None:
        rank = 'CHECK'
        if self.score < 0:
            rank = 'REJECT'
        elif 0 <= self.score <= 6:
            rank = 'WARNING'
        elif 7 <= self.score <= 9:
            rank = 'UNSURE'
        elif self.score > 10:
            rank = 'LIKELY'

        repo.apply_rank(self.score, rank)
