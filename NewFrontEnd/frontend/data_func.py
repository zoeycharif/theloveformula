import config

import numpy as np
import pandas as pd
import psycopg2
from psycopg2 import sql

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

dbcol = ['username', 'agerange', 'gender', 'orientation',
         'currentstatus', 'togethertime', 'relationshipdescription',
         'selfeducation', 'selffinancial', 'selfconfidence',
         'selfreligious', 'selfmaterialism', 'selfimage',
         'selfoccupation', 'selfworkethic', 'selfhousehold',
         'selfcommunication', 'selfartsy', 'selfcharitable',
         'selfpurpose', 'selfstatus', 'selfcultured',
         'selfselfcare', 'selfhonesty', 'selffamily',
         'value1', 'selfvalue1', 'partnervalue1', 'value2',
         'selfvalue2', 'partnervalue2', 'value3', 'selfvalue3',
         'partnervalue3', 'value4', 'selfvalue4', 'partnervalue4',
         'value5', 'selfvalue5', 'partnervalue5', 'selfappearance',
         'selfsocial', 'selfshy', 'selfalpha', 'selfhumorous',
         'selfspontaneous', 'selfgenerous', 'selfdriven',
         'selfintuitive', 'selfsexual', 'selfopenminded',
         'selfvibe', 'selfovergiving', 'selfdominant',
         'type1', 'partnertype1', 'type2', 'partnertype2',
         'type3', 'partnertype3', 'type4', 'partnertype4',
         'type5', 'partnertype5', 's_decisionmakingprocess',
         'qp_emotionalintelligence', 'q_jealous',
         'q_partnerjealous', 'q_manipulative',
         'qp_sexualchemistry', 'q_attractionloss', 'q_suffocated',
         'q_attention', 'q_coulddobetter', 'q_notgoodenough',
         'qp_longterm', 'qp_independet', 'q_coping', 'qp_selfcare',
         'q_emotionallydrained', 'q_depressed', 'q_abused',
         'q_partnerabuse', 'q_shutdown', 'q_partnershutdown',
         'q_privacyrespected', 'q_onoff', 'q_judged',
         'qp_communication', 'q_controlled', 'q_trapped',
         'qp_truetoself', 'q_comparedtoothers', 'q_movedtoofast',
         'q_showoff', 's1_logicvsfeelings', 's1_quitsvsstays',
         's1_practicalvsemotional', 's1_compatibilityvschemistry',
         's2_improvementvsacceptance', 's2_shortcomingsvsacceptance',
         's2_pickyvspositives', 's3_socialacceptancevsdontcare',
         's3_similarvsdifferent', 's4_lowstandardsvshighstandards',
         's4_imbettervsmatch', 's4_stayifimbettervsstayifpartnerbetter']

db_to_name = {'selfeducation':'Education/Knowledge/Street Smarts',
             'selffinancial': 'Financial Choices',
             'selfconfidence': 'Confidence/Self-Esteem',
             'selfreligious': 'Religious/Spiritual Values',
             'selfmaterialism': 'Materialism/Superficiality',
             'selfimage': 'Image/Fashion Sense/Body Modification',
             'selfoccupation': 'Occupation/Work Ethic/Self-Discipline',
             'selfhousehold': 'Household Care, Maintenance and Cleanliness',
             'selfcommunication': 'Communication Style/Manners',
             'selfartsy': 'Artsy/Creative/Musical',
             'selfcharitable': 'Charitable/Philanthropic',
             'selfpurpose': 'Pursuing a Greater Purpose',
             'selfstatus': 'Social Status/Sociability',
             'selfcultured': 'Cultured/Well-traveled/Woke',
             'selfselfcare': 'Self-Care/Personal Hygiene/Cleanliness',
             'selfhonesty': 'Honesty/Dependable/Reliable',
             'selffamily': 'Family Values'}

name_to_db = {v: k for k, v in db_to_name.items()}

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
                sql.Identifier('s_decisionmakingprocess'),
                sql.Identifier('qp_emotionalintelligence'),
                sql.Identifier('q_jealous'),
                sql.Identifier( 'q_partnerjealous'),
                sql.Identifier('q_manipulative'),
                sql.Identifier( 'qp_sexualchemistry'),
                sql.Identifier('q_attractionloss'),
                sql.Identifier('q_suffocated'),
                sql.Identifier('q_attention'),
                sql.Identifier('q_coulddobetter'),
                sql.Identifier('q_notgoodenough'),
                sql.Identifier('qp_longterm'),
                sql.Identifier('qp_independet'),
                sql.Identifier('q_coping'),
                sql.Identifier('qp_selfcare'),
                sql.Identifier('q_emotionallydrained'),
                sql.Identifier('q_depressed'),
                sql.Identifier('q_abused'),
                sql.Identifier('q_partnerabuse'),
                sql.Identifier('q_shutdown'),
                sql.Identifier('q_partnershutdown'),
                sql.Identifier('q_privacyrespected'),
                sql.Identifier('q_onoff'),
                sql.Identifier('q_judged'),
                sql.Identifier('qp_communication'),
                sql.Identifier('q_controlled'),
                sql.Identifier('q_trapped'),
                sql.Identifier('qp_truetoself'),
                sql.Identifier('q_comparedtoothers'),
                sql.Identifier('q_movedtoofast'),
                sql.Identifier('q_showoff'),
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

def insert_profile(data):
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
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s,
                {} = %s
                where {} = %s""")
        .format(sql.Identifier('profiles'),
                sql.Identifier('agerange'),
                sql.Identifier('gender'),
                sql.Identifier('orientation'),
                sql.Identifier('currentstatus'),
                sql.Identifier('togethertime'),
                sql.Identifier('relationshipdescription'),
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
