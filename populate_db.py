import config
from numpy.random import randint
import psycopg2
from psycopg2 import sql

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

def distinct(x):
    ls = []
    for e in x:
        if e in ls:
            continue
        else:
            ls.append(e)
    return len(ls)

conn = psycopg2.connect(user = config.user,
                      password = config.password,
                      host = config.hostname,
                      port = config.port,
                      database = config.database)

cur = conn.cursor()

cur.execute(sql.SQL("""select {},{},{},{},{},
                    {},{},{},{},{},{} from {}""").format(
                sql.Identifier('username'),
                sql.Identifier('value1'),
                sql.Identifier('value2'),
                sql.Identifier('value3'),
                sql.Identifier('value4'),
                sql.Identifier('value5'),
                sql.Identifier('selfvalue1'),
                sql.Identifier('selfvalue2'),
                sql.Identifier('selfvalue3'),
                sql.Identifier('selfvalue4'),
                sql.Identifier('selfvalue5'),
                sql.Identifier('profiles')
))
record = cur.fetchall()

nullrec = []

for x in record:
    print(x[0])
    if None in x or 'Other (please specify)' in x or distinct(x[1:6]) != 5:
        nullrec.append(x[0])
        continue
    cur.execute(sql.SQL("""update {} set
                        {} = %s,
                        {} = %s,
                        {} = %s,
                        {} = %s,
                        {} = %s
                        where {} = %s""").format(
                        sql.Identifier('profiles'),
                        sql.Identifier(name_to_db[x[1]]),
                        sql.Identifier(name_to_db[x[2]]),
                        sql.Identifier(name_to_db[x[3]]),
                        sql.Identifier(name_to_db[x[4]]),
                        sql.Identifier(name_to_db[x[5]]),
                        sql.Identifier('username'),
                        ),[x[6],x[7],x[8],x[9],x[10],x[0]])

    for col in dbcol[7:25]:
        cur.execute(sql.SQL(
            """update {} set {} = %s where {} is NULL and {} = %s """).format(
                sql.Identifier('profiles'),
                sql.Identifier(col),
                sql.Identifier(col),
                sql.Identifier('username')
            ), [randint(11),x[0]])

for r in nullrec:
    cur.execute(sql.SQL("delete from {} where {} = %s").format(
                        sql.Identifier('profiles'),
                        sql.Identifier('username')),[r]
    )

conn.commit()

if conn:
    cur.close()
    conn.close()
