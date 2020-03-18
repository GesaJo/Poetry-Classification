import argparse
from scrape_texts import scrape_texts_function
from clean_poems import clean_text_function
from joins_and_splits import agg_texts
from lyrics_model import train_model
from sklearn.feature_extraction.text import TfidfVectorizer

# Set up Parser
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--poet', type=str.lower, action='append')
args = parser.parse_args()

poets = args.poet

# Scraping and preparing the texts
print('Scraping...')
scrape_texts_function(poets)
print('Done!\n')

print('Texts are cleaned...')
clean_text_function(poets)

print('Further preprocessing...')
x_train, y_train, tfidf = agg_texts(poets)
print('Done!\n\nNow please enter a line of a poem:')

# input & vectorization
given_line = [input()]
given_li = tfidf.transform(given_line)
given = given_li.toarray()

# train model and predict poet
model = train_model(x_train, y_train, given)
