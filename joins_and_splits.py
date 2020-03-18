from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np

def agg_texts(list_of_poets):
    texts_aggregated = []
    y_aggregated = []

    for poet in list_of_poets:
        file = open(f'Poems/{poet}_cleaned.txt', 'r')
        x_str = file.read()
        file.close()

        # split string to make a list
        x_words = x_str.split(sep='], [')

        # add to texts_aggregated
        for text in x_words:
            texts_aggregated.append(text)

        # add y
        counter = len(x_words)
        for count in range(0, counter):
            y_aggregated.append(poet)

    # vectorize
    tfidf = TfidfVectorizer()
    fitted = tfidf.fit_transform(texts_aggregated)


    x_train = pd.DataFrame(fitted.todense(), columns=tfidf.get_feature_names())
    y_train = np.array(y_aggregated)
    
    return x_train, y_train, tfidf


# agg_texts(['sachs', 'ebner-eschenbach'])
