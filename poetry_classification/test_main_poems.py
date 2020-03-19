''' Tests for the poetry-classifier-program.'''
import os
import pytest
from check_poets import check_poets_function
from scrape_texts import scrape_texts_function
from clean_poems import clean_text_function
from joins_and_splits import agg_texts


# test scraping
"""def test_scrape_poets():
    if os.path.exists('Poems/claudius.txt'):
        os.remove('Poems/claudius.txt')
    scrape_texts_function(['claudius', 'sachs'])
    assert os.path.exists('Poems/claudius.txt')

    with pytest.raises(SystemExit):
        assert scrape_texts_function(['eich', 'sachs'])"""


# test check_poets
def test_check_poets():
    with pytest.raises(SystemExit):
        assert check_poets_function(['beethoven', 'fried'])
        assert check_poets_function(['kaléko', 'fried'])


# test cleaning
def test_clean_text():
    cleaned = clean_text_function('Ähm öl über Straße <a> Aufnahme 2000 \xa0')
    assert 'ä' and 'ö' and 'ü' and'ß' and '<a>' and 'Aufnahme 2000' and '\xa0'\
        not in cleaned


# test aggregating texts
def test_agg_texts():
    x, y, _ = agg_texts(['sachs', 'huch'])
    assert x.shape[0] == y.shape[0]
