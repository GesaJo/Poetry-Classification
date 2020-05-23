''' Main file for the poetry-classification-program. '''

import argparse
from os import path
from check_poets import check_poets_function, poets_list
from scrape_clean import scrape_texts_function
from tokenize_poems import tokenize_function
from aggregation_vectorization import agg_texts
from lyrics_model import train_model

# Set up Parser
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--poet', type=str.lower, action='append',
                    help='Type the names of two or more german poets,\
                            umlaute replaced by: ae, oe, ue.')
args = parser.parse_args()
poets = args.poet

# check if author exists on website
if path.exists("poets_list.txt"):
    pass
else:
    poets_list()
check_poets_function(poets)

# Scraping and cleaning of the texts, data augmentation
print('Scraping...')
texts = scrape_texts_function(poets)

# tokenizing
print('Texts are cleaned and tokenized...')
d_tokenized = tokenize_function(texts)
print('\n')
print('Further preprocessing...')
x_train, y_train, tfidf = agg_texts(d_tokenized)
print('\nNow please enter a line of a poem:')

# input & vectorization
given_line = [input()]
given_li = tfidf.transform(given_line)
given = given_li.toarray()

# train model and predict poet
train_model(x_train, y_train, given)
