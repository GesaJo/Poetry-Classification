''' Tests for the poetry-classifier-program.'''
import pytest
from check_poets import check_poets_function
from scrape_clean import scrape_texts_function, clean_text_function
from tokenize_poems import tokenize_function
from aggregation_vectorization import agg_texts


# test check_poets
def test_check_poets():
    with pytest.raises(SystemExit):
        assert check_poets_function(['beethoven', 'fried'])
        assert check_poets_function(['kaléko', 'fried'])


# test scraping
def test_scrape_poets():
    dict_poets = scrape_texts_function(['claudius', 'sachs'])
    assert list(dict_poets.keys()) == ['claudius', 'sachs']

    with pytest.raises(SystemExit):
        assert scrape_texts_function(['eich', 'sachs'])


# test cleaning
def test_clean_text():
    cleaned = clean_text_function('Ähm öl über Straße <a> Aufnahme 2000 \xa0')
    assert 'ä' and 'ö' and 'ü' and'ß' and '<a>' and 'Aufnahme 2000' and '\xa0'\
        not in cleaned


# test tokenizing
def test_tokenize_function():
    dict_tokenized = tokenize_function({'one': 'eins zwo', 'two': 'drei vier'})
    assert len(dict_tokenized) == 2


# test aggregating texts
def test_agg_texts():
    x, y, _ = agg_texts({'one': [['Mond Sonne']], 'two': [['Planet'], ['Schnuppe']]})
    assert x.shape[0] == y.shape[0]
