from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from imblearn.over_sampling import SMOTE


def train_model(x, y, pred):
    ''' Uses random oversampling (with SMOTE) to counteract class imbalance,
        then trains a Naive Bayes model with
        Gridsearch for alpha on the training data.'''

    sm = SMOTE(sampling_strategy="not majority")
    xsm, ysm = sm.fit_resample(x, y)

    # Train model
    alphas = [0.001, 0.01, 0.1, 0.2, 0.4, 0.5, 0.9]
    m = MultinomialNB()
    grid = GridSearchCV(estimator=m, param_grid=dict(alpha=alphas))
    grid.fit(xsm, ysm)
    ypred = grid.predict(pred)[0]
    cross_val = round(cross_val_score(m, xsm, ysm).mean()*100)
    if cross_val < 55:
        print("These authors are hard to distinguish - please try again.")
    else:
        print(f'\nThis line is most probably by {ypred.title()}!')
