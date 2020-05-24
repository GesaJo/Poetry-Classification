''' Main file for the poetry-classification-program. '''

import argparse
from check_poets import check_poets_function
from scrape_clean import scrape_texts_function
from tokenize_poems import tokenize_function
from aggregation_vectorization import agg_texts
from lyrics_model import train_model

# Set up Parser
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--poet', type=str.lower, action='append',
                    help='Type the last names of two or more german poets,\
                            umlaute replaced by: ae, oe, ue.')
args = parser.parse_args()

poets = args.poet

# check if author exists on website
check_poets_function(poets)

# Scraping and cleaning of the texts
print('Scraping...')
dictionary_poets = scrape_texts_function(poets)
print('Done!\n\n')

# tokenizing
print('Texts are cleaned and tokenized...')
dictionary_tokenized = tokenize_function(dictionary_poets)
print('\n')
print('Further preprocessing...')
x_train, y_train, tfidf = agg_texts(dictionary_tokenized)
print('Done!\n\nNow please enter a line of a poem:')

# input & vectorization
given_line = [input()]
given_t = tfidf.transform(given_line)
given = given_t.toarray()

# train model and predict poet
train_model(x_train, y_train, given)
