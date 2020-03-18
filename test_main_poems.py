''' Tests for the poetry-classifier-program.'''

from check_poets import check_poets_function
from scrape_texts import scrape_texts_function
from joins_and_splits import agg_texts
import os
import pytest


# test scraping
def test_scrape_poets():
    if os.path.exists('Poems/claudius.txt'):
        os.remove('Poems/claudius.txt')
    scrape_texts_function(['claudius', 'sachs'])
    assert os.path.exists('Poems/claudius.txt')


def test_scrape_poets2():
    with pytest.raises(SystemExit):
        assert scrape_texts_function(['eich', 'sachs'])


# test check_poets
def test_check_poets():
    with pytest.raises(SystemExit):
        assert check_poets_function(['beethoven', 'fried'])
        assert check_poets_function(['kaléko', 'fried'])


# test cleaning


# test aggregating texts
def test_agg_texts():
    x, y, _ = agg_texts(['sachs', 'huch'])
    assert x.shape[0] == y.shape[0]

# test input

# test model
