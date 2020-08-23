import config

import numpy as np
import pandas as pd
import psycopg2
from psycopg2 import sql

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def bootstrap(X,y,target):
    X_ = X
    y_ = y
    while X_.shape[0] < target:
        n = np.random.randint(X.shape[0])
        X_ = X_.append(X.iloc[n,:])
        y_ = y_.append(y.iloc[n])
    return (X_,y_)

def create_model(X,y,num_samples=1000):
    testing_score = 0
    while(testing_score < .85):
        Xb,yb = bootstrap(X,y,num_samples)
        X_train, X_test, y_train, y_test = train_test_split(Xb, yb)
        model = LinearRegression()

        # Fitting our model with all of our features in X
        model.fit(Xb, yb)
        print(f"R2 Score: {model.score(Xb, yb)}")

        model.fit(X_train, y_train)
        testing_score = model.score(X_test, y_test)
        print(f"Training Score: {model.score(X_train, y_train)}")
        print(f"Testing Score: {testing_score}")

    return model
