from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, train_test_split

def train_model(X, y, test_size=0.3, random_state=1):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    pipe_svc = Pipeline([
        ('scl', StandardScaler()),
        ('clf', SVC())])

    param_grid = [
        {'clf__kernel': ['linear'], 'clf__C': [0.01, 0.1, 1, 10]},
        {'clf__kernel': ['rbf'], 'clf__C': [0.01, 0.1, 1, 10], 'clf__gamma': [0.01, 0.1, 1]}
    ]
    gs = GridSearchCV(estimator=pipe_svc, param_grid=param_grid, scoring='accuracy', cv=3)
    gs.fit(X_train, y_train)

    best_model = gs.best_estimator_
    return best_model, gs, X_test, y_test
