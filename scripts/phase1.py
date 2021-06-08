# Justin Ventura | Carnegie Mellon University

# Libraries:
import numpy as np
import pandas as pd
import stscraper as scraper

"""
DESCRIPTION:
This script will be used to scrape (primarily) github
for software with the criteria we need it to fit.

THE CHALLENGE: we are NOT looking for frameworks, APIs,
school projects, student work, demos for research papers
or thesis', notebook experiments, nor hackathon projects.

WHAT WE WANT: open source commercial software with some
sort of ML/AI implementation.  Simple filters will not
yield desired results, so we are still trying to figure
out an effective way to scrape.  Brute forcing is not
an option since it would require human validation which
is astronomically slow, and painful.

IDEAS:

1) possibly a scoring system to rank repos found based
   on keywords (in desc/readme), topics (if any), number
   of stars, contributors, and forks, and potentially
   check through source code for signs of ML/AI.  Maybe
   look for inclusion of libraries.  Still need to find
   a way to filter out libraries, projects, frameworks,
   etc.
"""


# This is the first version of the search.
def search_v1():
    pass


# TODO: perform a basic search through tags using kws.
def _main():
    _ = search_v1()


# Run script directly.
if __name__ == '__main__':
    _main()