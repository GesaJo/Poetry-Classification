''' Creates suitable training-data'''

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np


def agg_texts(dict_tokenized):
    ''' Aggregates texts from given poets and
        creates y-values according to the authors.
        Vectorizes the poems and shapes them into suitable training-data.
        Input: list of poet-names,
        output: x_train, y_train and the vectorizer.'''

    texts_aggregated = []
    y_aggregated = []

    for poet in dict_tokenized:
        # add to texts_aggregated and create y-values
        for text in dict_tokenized[poet]:
            for subtext in text:
                texts_aggregated.append(subtext)
                y_aggregated.append(poet)

    # vectorize
    tfidf = TfidfVectorizer()
    fitted = tfidf.fit_transform(texts_aggregated)

    # shape into training-data
    x_train = pd.DataFrame(fitted.todense(), columns=tfidf.get_feature_names())
    y_train = np.array(y_aggregated)

    return x_train, y_train, tfidf
