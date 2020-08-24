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

def insertData(data):
    conn = psycopg2.connect(user = config.user,
                              password = config.password,
                              host = config.hostname,
                              port = config.port,
                              database = config.database)

    cur = conn.cursor()
    cur.execute(
        sql.SQL("""update {} set
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s
                where {} = %s""")
        .format(sql.Identifier('profiles'),
                sql.Identifier('value1'),
                sql.Identifier('selfvalue1'),
                sql.Identifier('partnervalue1'),
                sql.Identifier('value2'),
                sql.Identifier('selfvalue2'),
                sql.Identifier('partnervalue2'),
                sql.Identifier('value3'),
                sql.Identifier('selfvalue3'),
                sql.Identifier('partnervalue3'),
                sql.Identifier('value4'),
                sql.Identifier('selfvalue4'),
                sql.Identifier('partnervalue4'),
                sql.Identifier('value5'),
                sql.Identifier('selfvalue5'),
                sql.Identifier('partnervalue5'),
                sql.Identifier('type1'),
                sql.Identifier('partnertype1'),
                sql.Identifier('type2'),
                sql.Identifier('partnertype2'),
                sql.Identifier('type3'),
                sql.Identifier('partnertype3'),
                sql.Identifier('type4'),
                sql.Identifier('partnertype4'),
                sql.Identifier('type5'),
                sql.Identifier('partnertype5'),
                sql.Identifier('s1_logicvsfeelings'),
                sql.Identifier('s1_quitsvsstays'),
                sql.Identifier('s1_practicalvsemotional'),
                sql.Identifier('s1_compatibilityvschemistry'),
                sql.Identifier('s2_improvementvsacceptance'),
                sql.Identifier('s2_shortcomingsvsacceptance'),
                sql.Identifier('s2_pickyvspositives'),
                sql.Identifier('s3_socialacceptancevsdontcare'),
                sql.Identifier('s3_similarvsdifferent'),
                sql.Identifier('s4_lowstandardsvshighstandards'),
                sql.Identifier('s4_imbettervsmatch'),
                sql.Identifier('s4_stayifimbettervsstayifpartnerbetter'),
                sql.Identifier('username')),
        data)
    conn.commit()

    if(conn):
        cur.close()
        conn.close()
    return 1
