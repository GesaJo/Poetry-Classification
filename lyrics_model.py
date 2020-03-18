from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import GridSearchCV
from imblearn.over_sampling import RandomOverSampler
from sklearn.model_selection import cross_val_score
from sklearn.metrics import f1_score



def train_model(x, y, pred):
    # Balance Dataset with SMOTE
    sm = RandomOverSampler(sampling_strategy='minority')
    xsm, ysm = sm.fit_resample(x, y)


    # Naive Bayes with Gridsearch
    alphas = [0.001, 0.01, 0.1, 0.2, 0.4, 0.5, 0.9]
    m = MultinomialNB()
    grid = GridSearchCV(estimator=m, param_grid=dict(alpha=alphas))
    grid.fit(xsm, ysm)
    ypred = grid.predict(pred)[0]

    print(cross_val_score(m, xsm, ysm).mean())
    print(f'This poem is by {ypred.title()}!')
