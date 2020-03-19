from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from imblearn.over_sampling import RandomOverSampler


def train_model(x, y, pred):
    ''' Uses random oversampling to counteract class imbalance,
        then trains a Naive Bayes model with
        Gridsearch for alpha on the training data.
        Also prints crossvalidation-score (might be deleted later).'''

    # Balance Dataset with RandomOversampling
    sm = RandomOverSampler(sampling_strategy='minority')
    xsm, ysm = sm.fit_resample(x, y)

    # Train model
    alphas = [0.001, 0.01, 0.1, 0.2, 0.4, 0.5, 0.9]
    m = MultinomialNB()
    grid = GridSearchCV(estimator=m, param_grid=dict(alpha=alphas))
    grid.fit(xsm, ysm)
    ypred = grid.predict(pred)[0]

    cross_val = round(cross_val_score(m, xsm, ysm).mean()*100)
    print(f'\nWith a probability of {cross_val}% is this line by {ypred.title()}!')
