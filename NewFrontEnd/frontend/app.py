# import Libraries/Dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

import config
import data_func

from flask import Flask, render_template, jsonify, redirect, request, url_for, session, flash
from datetime import timedelta
import pickle
#################################################
# Flask Setup
#################################################
app = Flask(__name__)
app.secret_key = "hihi"
# app.permanent_session_lifetime = timedelta(days=1)

#################################################
# Database Setup
#################################################


#table names are #profiles #users

# from flask_sqlalchemy import SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgres://jyfiybgxgthlpk:803a3b11c71fa39768bb853656d3db2dcab91c1a40640b8314a7fbcc509ed242@ec2-3-215-207-12.compute-1.amazonaws.com:5432/d721k5b7avhgf8')

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# from .models import


URI = "postgres://rhjtenpwhdlbjl:4d3153a71d04ee752de8aab6fb6ac3baaff5fe615aa7a6223845aab661e0c6af@ec2-34-237-89-96.compute-1.amazonaws.com:5432/d1l8p7t7cs19l8"

engine = create_engine(URI)

session = Session(engine)
inspector = inspect(engine)
columns = inspector.get_columns("profiles")
for c in columns:
    print(c["name"])
Base = automap_base()
Base.prepare(engine, reflect = True)
print(Base.classes.keys())
Profiles = Base.classes.profiles





# create route that renders index.html template
@app.route("/")
def home():

    return render_template("index.html")

@app.route("/newuser")
def newuser():

    return render_template("newuser.html")

@app.route("/returnuser")
def returnuser():

    return render_template("returnuser.html")


@app.route("/ratings")
def ratings():

    return render_template("rating.html")


@app.route("/formsubmit", methods= ["POST", "GET"])
def formsubmit():
    session = Session(engine)
    results = session.query(Profiles.qp_communication).all()
    # print(results)
    lovedata = []
    lovedata.append(request.form["Value1"])
    lovedata.append(request.form["SelfValue1"])
    lovedata.append(request.form["PartnerValue1"])
    lovedata.append(request.form["Value2"])
    lovedata.append(request.form["SelfValue2"])
    lovedata.append(request.form["PartnerValue2"])
    lovedata.append(request.form["Value3"])
    lovedata.append(request.form["SelfValue3"])
    lovedata.append(request.form["PartnerValue3"])
    lovedata.append(request.form["Value4"])
    lovedata.append(request.form["SelfValue4"])
    lovedata.append(request.form["PartnerValue4"])
    lovedata.append(request.form["Value5"])
    lovedata.append(request.form["SelfValue5"])
    lovedata.append(request.form["PartnerValue5"])
    lovedata.append(request.form["Type1"])
    lovedata.append(request.form["PartnerType1"])
    lovedata.append(request.form["Type2"])
    lovedata.append(request.form["PartnerType2"])
    lovedata.append(request.form["Type3"])
    lovedata.append(request.form["PartnerType3"])
    lovedata.append(request.form["Type4"])
    lovedata.append(request.form["PartnerType4"])
    lovedata.append(request.form["Type5"])
    lovedata.append(request.form["PartnerType5"])
    lovedata.append(request.form["S1_LogicVsFeelings"])
    lovedata.append(request.form["S1_QuitsVsStays"])
    lovedata.append(request.form["S1_PracticalVsEmotional"])
    lovedata.append(request.form["S1_CompatibilityVsChemistry"])
    lovedata.append(request.form["S2_ImprovementVsAcceptance"])
    lovedata.append(request.form["S2_ShortcomingsVSAcceptance"])
    lovedata.append(request.form["S2_PickyVsPositives"])
    lovedata.append(request.form["S3_SocialAcceptanceVsDontCare"])
    lovedata.append(request.form["S3_SimilarVsDifferent"])
    lovedata.append(request.form["S4_LowStandardsVsHighStandards"])
    lovedata.append(request.form["S4_ImBetterVsMatch"])
    lovedata.append(request.form["S4_StayIfImBetterVsStayIfPartnerBetter"])
    print (lovedata)
    insertData(lovedata)
    session.close()
    #db.session.add(profiles)
    #db.session.commit()

#populate the data to be put into machine learning model
#value 1
    mldata = [0]*51
    if request.form["Value1"] == "Education/Knowledge/Street Smarts":
        mldata[0] = float(request.form["SelfValue1"])
        mldata[1] = float(request.form["PartnerValue1"])
        mldata[2] = abs(mldata[0] - mldata[1]*.99)
    if request.form["Value1"] == "Financial Choices":
        mldata[3] = float(request.form["SelfValue1"])
        mldata[4] = float(request.form["PartnerValue1"])
        mldata[5] = abs(mldata[3] - mldata[4]*.99)
    if request.form["Value1"] == "Confidence/Self-Esteem":
        mldata[6] = float(request.form["SelfValue1"])
        mldata[7] = float(request.form["PartnerValue1"])
        mldata[8] = abs(mldata[6] - mldata[7]*.99)
    if request.form["Value1"] =="Religious/Spiritual Values":
        mldata[9] = float(request.form["SelfValue1"])
        mldata[10] = float(request.form["PartnerValue1"])
        mldata[11] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value1"] == "Materialism/Superficiality":
        mldata[12] = float(request.form["SelfValue1"])
        mldata[13] = float(request.form["PartnerValue1"])
        mldata[14] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value1"] == "Image/Fashion Sense/Body Modification":
        mldata[15] = float(request.form["SelfValue1"])
        mldata[16] = float(request.form["PartnerValue1"])
        mldata[17] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value1"] == "Occupation/Work Ethic/Self-Discipline":
        mldata[18] = float(request.form["SelfValue1"])
        mldata[19] = float(request.form["PartnerValue1"])
        mldata[20] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value1"] == "Household Care, Maintenance and Cleanliness":
        mldata[21] = float(request.form["SelfValue1"])
        mldata[22] = float(request.form["PartnerValue1"])
        mldata[23] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value1"] == "Communication Style/Manners":
        mldata[24] = float(request.form["SelfValue1"])
        mldata[25] = float(request.form["PartnerValue1"])
        mldata[26] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value1"] == "Artsy/Creative/Musical":
        mldata[27] = float(request.form["SelfValue1"])
        mldata[28] = float(request.form["PartnerValue1"])
        mldata[29] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value1"] == "Charitable/Philanthropic":
        mldata[30] = float(request.form["SelfValue1"])
        mldata[31] = float(request.form["PartnerValue1"])
        mldata[32] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value1"] == "Pursuing a Greater Purpose":
        mldata[33] = float(request.form["SelfValue1"])
        mldata[34] = float(request.form["PartnerValue1"])
        mldata[35] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value1"] == "Social Status/Sociability":
        mldata[36] = float(request.form["SelfValue1"])
        mldata[37] = float(request.form["PartnerValue1"])
        mldata[38] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value1"] == "Cultured/Well-traveled/Woke":
        mldata[39] = float(request.form["SelfValue1"])
        mldata[40] = float(request.form["PartnerValue1"])
        mldata[41] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value1"] == "Self-Care/Personal Hygiene/Cleanliness":
        mldata[42] = float(request.form["SelfValue1"])
        mldata[43] = float(request.form["PartnerValue1"])
        mldata[44] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value1"] == "Honesty/Dependable/Reliable":
        mldata[45] = float(request.form["SelfValue1"])
        mldata[46] = float(request.form["PartnerValue1"])
        mldata[47] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value1"] == "Family Values":
        mldata[48] = float(request.form["SelfValue1"])
        mldata[49] = float(request.form["PartnerValue1"])
        mldata[50] = abs(mldata[9] - mldata[10]*.99)

#for value 2
    if request.form["Value2"] == "Education/Knowledge/Street Smarts":
        mldata[0] = float(request.form["SelfValue1"])
        mldata[1] = float(request.form["PartnerValue1"])
        mldata[2] = abs(mldata[0] - mldata[1]*.99)
    if request.form["Value2"] == "Financial Choices":
        mldata[3] = float(request.form["SelfValue1"])
        mldata[4] = float(request.form["PartnerValue1"])
        mldata[5] = abs(mldata[3] - mldata[4]*.99)
    if request.form["Value2"] == "Confidence/Self-Esteem":
        mldata[6] = float(request.form["SelfValue1"])
        mldata[7] = float(request.form["PartnerValue1"])
        mldata[8] = abs(mldata[6] - mldata[7]*.99)
    if request.form["Value2"] =="Religious/Spiritual Values":
        mldata[9] = float(request.form["SelfValue1"])
        mldata[10] = float(request.form["PartnerValue1"])
        mldata[11] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value2"] == "Materialism/Superficiality":
        mldata[12] = float(request.form["SelfValue1"])
        mldata[13] = float(request.form["PartnerValue1"])
        mldata[14] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value2"] == "Image/Fashion Sense/Body Modification":
        mldata[15] = float(request.form["SelfValue1"])
        mldata[16] = float(request.form["PartnerValue1"])
        mldata[17] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value2"] == "Occupation/Work Ethic/Self-Discipline":
        mldata[18] = float(request.form["SelfValue1"])
        mldata[19] = float(request.form["PartnerValue1"])
        mldata[20] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value2"] == "Household Care, Maintenance and Cleanliness":
        mldata[21] = float(request.form["SelfValue1"])
        mldata[22] = float(request.form["PartnerValue1"])
        mldata[23] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value2"] == "Communication Style/Manners":
        mldata[24] = float(request.form["SelfValue1"])
        mldata[25] = float(request.form["PartnerValue1"])
        mldata[26] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value2"] == "Artsy/Creative/Musical":
        mldata[27] = float(request.form["SelfValue1"])
        mldata[28] = float(request.form["PartnerValue1"])
        mldata[29] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value2"] == "Charitable/Philanthropic":
        mldata[30] = float(request.form["SelfValue1"])
        mldata[31] = float(request.form["PartnerValue1"])
        mldata[32] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value2"] == "Pursuing a Greater Purpose":
        mldata[33] = float(request.form["SelfValue1"])
        mldata[34] = float(request.form["PartnerValue1"])
        mldata[35] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value2"] == "Social Status/Sociability":
        mldata[36] = float(request.form["SelfValue1"])
        mldata[37] = float(request.form["PartnerValue1"])
        mldata[38] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value2"] == "Cultured/Well-traveled/Woke":
        mldata[39] = float(request.form["SelfValue1"])
        mldata[40] = float(request.form["PartnerValue1"])
        mldata[41] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value2"] == "Self-Care/Personal Hygiene/Cleanliness":
        mldata[42] = float(request.form["SelfValue1"])
        mldata[43] = float(request.form["PartnerValue1"])
        mldata[44] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value2"] == "Honesty/Dependable/Reliable":
        mldata[45] = float(request.form["SelfValue1"])
        mldata[46] = float(request.form["PartnerValue1"])
        mldata[47] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value2"] == "Family Values":
        mldata[48] = float(request.form["SelfValue1"])
        mldata[49] = float(request.form["PartnerValue1"])
        mldata[50] = abs(mldata[9] - mldata[10]*.99)

#for value 2
    if request.form["Value3"] == "Education/Knowledge/Street Smarts":
        mldata[0] = float(request.form["SelfValue1"])
        mldata[1] = float(request.form["PartnerValue1"])
        mldata[2] = abs(mldata[0] - mldata[1]*.99)
    if request.form["Value3"] == "Financial Choices":
        mldata[3] = float(request.form["SelfValue1"])
        mldata[4] = float(request.form["PartnerValue1"])
        mldata[5] = abs(mldata[3] - mldata[4]*.99)
    if request.form["Value3"] == "Confidence/Self-Esteem":
        mldata[6] = float(request.form["SelfValue1"])
        mldata[7] = float(request.form["PartnerValue1"])
        mldata[8] = abs(mldata[6] - mldata[7]*.99)
    if request.form["Value3"] =="Religious/Spiritual Values":
        mldata[9] = float(request.form["SelfValue1"])
        mldata[10] = float(request.form["PartnerValue1"])
        mldata[11] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value3"] == "Materialism/Superficiality":
        mldata[12] = float(request.form["SelfValue1"])
        mldata[13] = float(request.form["PartnerValue1"])
        mldata[14] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value3"] == "Image/Fashion Sense/Body Modification":
        mldata[15] = float(request.form["SelfValue1"])
        mldata[16] = float(request.form["PartnerValue1"])
        mldata[17] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value3"] == "Occupation/Work Ethic/Self-Discipline":
        mldata[18] = float(request.form["SelfValue1"])
        mldata[19] = float(request.form["PartnerValue1"])
        mldata[20] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value3"] == "Household Care, Maintenance and Cleanliness":
        mldata[21] = float(request.form["SelfValue1"])
        mldata[22] = float(request.form["PartnerValue1"])
        mldata[23] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value3"] == "Communication Style/Manners":
        mldata[24] = float(request.form["SelfValue1"])
        mldata[25] = float(request.form["PartnerValue1"])
        mldata[26] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value3"] == "Artsy/Creative/Musical":
        mldata[27] = float(request.form["SelfValue1"])
        mldata[28] = float(request.form["PartnerValue1"])
        mldata[29] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value3"] == "Charitable/Philanthropic":
        mldata[30] = float(request.form["SelfValue1"])
        mldata[31] = float(request.form["PartnerValue1"])
        mldata[32] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value3"] == "Pursuing a Greater Purpose":
        mldata[33] = float(request.form["SelfValue1"])
        mldata[34] = float(request.form["PartnerValue1"])
        mldata[35] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value3"] == "Social Status/Sociability":
        mldata[36] = float(request.form["SelfValue1"])
        mldata[37] = float(request.form["PartnerValue1"])
        mldata[38] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value3"] == "Cultured/Well-traveled/Woke":
        mldata[39] = float(request.form["SelfValue1"])
        mldata[40] = float(request.form["PartnerValue1"])
        mldata[41] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value3"] == "Self-Care/Personal Hygiene/Cleanliness":
        mldata[42] = float(request.form["SelfValue1"])
        mldata[43] = float(request.form["PartnerValue1"])
        mldata[44] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value3"] == "Honesty/Dependable/Reliable":
        mldata[45] = float(request.form["SelfValue1"])
        mldata[46] = float(request.form["PartnerValue1"])
        mldata[47] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value3"] == "Family Values":
        mldata[48] = float(request.form["SelfValue1"])
        mldata[49] = float(request.form["PartnerValue1"])
        mldata[50] = abs(mldata[9] - mldata[10]*.99)

    #for value 4
    if request.form["Value4"] == "Education/Knowledge/Street Smarts":
        mldata[0] = float(request.form["SelfValue1"])
        mldata[1] = float(request.form["PartnerValue1"])
        mldata[2] = abs(mldata[0] - mldata[1]*.99)
    if request.form["Value4"] == "Financial Choices":
        mldata[3] = float(request.form["SelfValue1"])
        mldata[4] = float(request.form["PartnerValue1"])
        mldata[5] = abs(mldata[3] - mldata[4]*.99)
    if request.form["Value4"] == "Confidence/Self-Esteem":
        mldata[6] = float(request.form["SelfValue1"])
        mldata[7] = float(request.form["PartnerValue1"])
        mldata[8] = abs(mldata[6] - mldata[7]*.99)
    if request.form["Value4"] =="Religious/Spiritual Values":
        mldata[9] = float(request.form["SelfValue1"])
        mldata[10] = float(request.form["PartnerValue1"])
        mldata[11] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value4"] == "Materialism/Superficiality":
        mldata[12] = float(request.form["SelfValue1"])
        mldata[13] = float(request.form["PartnerValue1"])
        mldata[14] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value4"] == "Image/Fashion Sense/Body Modification":
        mldata[15] = float(request.form["SelfValue1"])
        mldata[16] = float(request.form["PartnerValue1"])
        mldata[17] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value4"] == "Occupation/Work Ethic/Self-Discipline":
        mldata[18] = float(request.form["SelfValue1"])
        mldata[19] = float(request.form["PartnerValue1"])
        mldata[20] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value4"] == "Household Care, Maintenance and Cleanliness":
        mldata[21] = float(request.form["SelfValue1"])
        mldata[22] = float(request.form["PartnerValue1"])
        mldata[23] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value4"] == "Communication Style/Manners":
        mldata[24] = float(request.form["SelfValue1"])
        mldata[25] = float(request.form["PartnerValue1"])
        mldata[26] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value3"] == "Artsy/Creative/Musical":
        mldata[27] = float(request.form["SelfValue1"])
        mldata[28] = float(request.form["PartnerValue1"])
        mldata[29] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value4"] == "Charitable/Philanthropic":
        mldata[30] = float(request.form["SelfValue1"])
        mldata[31] = float(request.form["PartnerValue1"])
        mldata[32] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value4"] == "Pursuing a Greater Purpose":
        mldata[33] = float(request.form["SelfValue1"])
        mldata[34] = float(request.form["PartnerValue1"])
        mldata[35] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value4"] == "Social Status/Sociability":
        mldata[36] = float(request.form["SelfValue1"])
        mldata[37] = float(request.form["PartnerValue1"])
        mldata[38] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value4"] == "Cultured/Well-traveled/Woke":
        mldata[39] = float(request.form["SelfValue1"])
        mldata[40] = float(request.form["PartnerValue1"])
        mldata[41] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value4"] == "Self-Care/Personal Hygiene/Cleanliness":
        mldata[42] = float(request.form["SelfValue1"])
        mldata[43] = float(request.form["PartnerValue1"])
        mldata[44] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value4"] == "Honesty/Dependable/Reliable":
        mldata[45] = float(request.form["SelfValue1"])
        mldata[46] = float(request.form["PartnerValue1"])
        mldata[47] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value4"] == "Family Values":
        mldata[48] = float(request.form["SelfValue1"])
        mldata[49] = float(request.form["PartnerValue1"])
        mldata[50] = abs(mldata[9] - mldata[10]*.99)

    #for value 5
    if request.form["Value5"] == "Education/Knowledge/Street Smarts":
        mldata[0] = float(request.form["SelfValue1"])
        mldata[1] = float(request.form["PartnerValue1"])
        mldata[2] = abs(mldata[0] - mldata[1]*.99)
    if request.form["Value5"] == "Financial Choices":
        mldata[3] = float(request.form["SelfValue1"])
        mldata[4] = float(request.form["PartnerValue1"])
        mldata[5] = abs(mldata[3] - mldata[4]*.99)
    if request.form["Value5"] == "Confidence/Self-Esteem":
        mldata[6] = float(request.form["SelfValue1"])
        mldata[7] = float(request.form["PartnerValue1"])
        mldata[8] = abs(mldata[6] - mldata[7]*.99)
    if request.form["Value5"] =="Religious/Spiritual Values":
        mldata[9] = float(request.form["SelfValue1"])
        mldata[10] = float(request.form["PartnerValue1"])
        mldata[11] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value5"] == "Materialism/Superficiality":
        mldata[12] = float(request.form["SelfValue1"])
        mldata[13] = float(request.form["PartnerValue1"])
        mldata[14] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value5"] == "Image/Fashion Sense/Body Modification":
        mldata[15] = float(request.form["SelfValue1"])
        mldata[16] = float(request.form["PartnerValue1"])
        mldata[17] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value5"] == "Occupation/Work Ethic/Self-Discipline":
        mldata[18] = float(request.form["SelfValue1"])
        mldata[19] = float(request.form["PartnerValue1"])
        mldata[20] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value5"] == "Household Care, Maintenance and Cleanliness":
        mldata[21] = float(request.form["SelfValue1"])
        mldata[22] = float(request.form["PartnerValue1"])
        mldata[23] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value5"] == "Communication Style/Manners":
        mldata[24] = float(request.form["SelfValue1"])
        mldata[25] = float(request.form["PartnerValue1"])
        mldata[26] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value5"] == "Artsy/Creative/Musical":
        mldata[27] = float(request.form["SelfValue1"])
        mldata[28] = float(request.form["PartnerValue1"])
        mldata[29] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value5"] == "Charitable/Philanthropic":
        mldata[30] = float(request.form["SelfValue1"])
        mldata[31] = float(request.form["PartnerValue1"])
        mldata[32] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value5"] == "Pursuing a Greater Purpose":
        mldata[33] = float(request.form["SelfValue1"])
        mldata[34] = float(request.form["PartnerValue1"])
        mldata[35] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value5"] == "Social Status/Sociability":
        mldata[36] = float(request.form["SelfValue1"])
        mldata[37] = float(request.form["PartnerValue1"])
        mldata[38] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value5"] == "Cultured/Well-traveled/Woke":
        mldata[39] = float(request.form["SelfValue1"])
        mldata[40] = float(request.form["PartnerValue1"])
        mldata[41] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value5"] == "Self-Care/Personal Hygiene/Cleanliness":
        mldata[42] = float(request.form["SelfValue1"])
        mldata[43] = float(request.form["PartnerValue1"])
        mldata[44] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value5"] == "Honesty/Dependable/Reliable":
        mldata[45] = float(request.form["SelfValue1"])
        mldata[46] = float(request.form["PartnerValue1"])
        mldata[47] = abs(mldata[9] - mldata[10]*.99)
    if request.form["Value5"] == "Family Values":
        mldata[48] = float(request.form["SelfValue1"])
        mldata[49] = float(request.form["PartnerValue1"])
        mldata[50] = abs(mldata[9] - mldata[10]*.99)

    #pickle will load the model template and run it on mldata saved in the static file.
    loaded_model = pickle.load(open("static/data/finalized_model.sav", 'rb'))
    result = loaded_model.predict(list(mldata))
    print(result[0][0])
    return render_template("rating.html", LoveRating = result[0][0])


@app.route("/survey")
def survey():
    return render_template("survey.html")


@app.route("/formsubmit1", methods= ["POST", "GET"])
def formsubmit1():
    # session = Session(engine)
    # results = session.query(Profiles.qp_communication).all()
    # print(results)
    surveydata = []
    surveydata.append(request.form["AgeRange"])
    surveydata.append(request.form["Gender"])
    surveydata.append(request.form["Orientation"])
    surveydata.append(request.form["CurrentStatus"])
    surveydata.append(request.form["TogetherTime"])
    surveydata.append(request.form["RelationshipDescription"])
    surveydata.append(request.form["Value1"])
    surveydata.append(request.form["SelfValue1"])
    surveydata.append(request.form["PartnerValue1"])
    surveydata.append(request.form["Value2"])
    surveydata.append(request.form["SelfValue2"])
    surveydata.append(request.form["PartnerValue2"])
    surveydata.append(request.form["Value3"])
    surveydata.append(request.form["SelfValue3"])
    surveydata.append(request.form["PartnerValue3"])
    surveydata.append(request.form["Value4"])
    surveydata.append(request.form["SelfValue4"])
    surveydata.append(request.form["PartnerValue4"])
    surveydata.append(request.form["Value5"])
    surveydata.append(request.form["SelfValue5"])
    surveydata.append(request.form["PartnerValue5"])
    surveydata.append(request.form["Type1"])
    surveydata.append(request.form["PartnerType1"])
    surveydata.append(request.form["Type2"])
    surveydata.append(request.form["PartnerType2"])
    surveydata.append(request.form["Type3"])
    surveydata.append(request.form["PartnerType3"])
    surveydata.append(request.form["Type4"])
    surveydata.append(request.form["PartnerType4"])
    surveydata.append(request.form["Type5"])
    surveydata.append(request.form["PartnerType5"])
    surveydata.append(request.form["S_DecisionMakingProcess"])
    surveydata.append(request.form.get("QP_EmotionalIntelligence"))
    surveydata.append(request.form.get("Q_Jealous"))
    surveydata.append(request.form.get("Q_PartnerJealous"))
    # surveydata.append(request.form.get("Q_PartnerJealous- checklater"))
    surveydata.append(request.form.get("Q_Manipulative"))
    surveydata.append(request.form.get("QP_SexualChemistry"))
    surveydata.append(request.form.get("Q_AttractionLoss"))
    surveydata.append(request.form.get("Q_Suffocated"))
    surveydata.append(request.form.get("Q_Attention"))
    surveydata.append(request.form.get("Q_CouldDoBetter"))
    surveydata.append(request.form.get("Q_NotGoodEnough"))
    surveydata.append(request.form.get("QP_Longterm"))
    surveydata.append(request.form.get("QP_Independent"))
    surveydata.append(request.form.get("Q_Coping"))
    surveydata.append(request.form.get("QP_SelfCare"))
    surveydata.append(request.form.get("Q_EmotionallyDrained"))
    surveydata.append(request.form.get("Q_Depressed"))
    surveydata.append(request.form.get("Q_Abused"))
    surveydata.append(request.form.get("Q_PartnerAbuse"))
    surveydata.append(request.form.get("Q_ShutDown"))
    surveydata.append(request.form.get("Q_PartnerShutDown"))
    surveydata.append(request.form.get("Q_PrivacyRespected"))
    surveydata.append(request.form.get("Q_OnOff"))
    surveydata.append(request.form.get("Q_Judged"))
    surveydata.append(request.form.get("QP_Communication"))
    surveydata.append(request.form.get("Q_Controlled"))
    surveydata.append(request.form.get("Q_Trapped"))
    surveydata.append(request.form.get("QP_TrueToSelf"))
    surveydata.append(request.form.get("Q_ComparedToOthers"))
    surveydata.append(request.form.get("Q_MovedTooFast"))
    surveydata.append(request.form.get("Q_ShowOff"))
    surveydata.append(request.form["S1_LogicVsFeelings"])
    surveydata.append(request.form["S1_QuitsVsStays"])
    surveydata.append(request.form["S1_PracticalVsEmotional"])
    surveydata.append(request.form["S1_CompatibilityVsChemistry"])
    surveydata.append(request.form["S2_ImprovementVsAcceptance"])
    surveydata.append(request.form["S2_ShortcomingsVSAcceptance"])
    surveydata.append(request.form["S2_ShortcomingsVSAcceptance"])
    surveydata.append(request.form["S2_PickyVsPositives"])
    surveydata.append(request.form["S3_SocialAcceptanceVsDontCare"])
    surveydata.append(request.form["S3_SimilarVsDifferent"])
    surveydata.append(request.form["S4_LowStandardsVsHighStandards"])
    surveydata.append(request.form["S4_ImBetterVsMatch"])
    surveydata.append(request.form["S4_StayIfImBetterVsStayIfPartnerBetter"])

    print(surveydata)
    session.close()
    #db.session.add(profiles)
    #db.session.commit()
    return render_template("survey.html")

@app.route("/profile", methods=["GET", "POST"])
def personality():

    return render_template("profile.html")

@app.route("/formsubmit2", methods= ["POST", "GET"])
def formsubmit2():

    profiledata = []
    profiledata.append(request.form["AgeRange"])
    profiledata.append(request.form["Gender"])
    profiledata.append(request.form["Orientation"])
    profiledata.append(request.form["SelfEducation"])
    profiledata.append(request.form["SelfFinancial"])
    profiledata.append(request.form["SelfConfidence"])
    profiledata.append(request.form["SelfReligious"])
    profiledata.append(request.form["SelfMaterialism"])
    profiledata.append(request.form["SelfImage"])
    profiledata.append(request.form["SelfOccupation"])
    profiledata.append(request.form["SelfWorkethic"])
    profiledata.append(request.form["SelfHousehold"])
    profiledata.append(request.form["SelfCommunication"])
    profiledata.append(request.form["SelfArtsy"])
    profiledata.append(request.form["SelfCharitable"])
    profiledata.append(request.form["SelfPurpose"])
    profiledata.append(request.form["SelfStatus"])
    profiledata.append(request.form["SelfCultured"])
    profiledata.append(request.form["SelfCare"])
    profiledata.append(request.form["SelfHonesty"])
    profiledata.append(request.form["SelfFamily"])
    profiledata.append(request.form["Value1"])
    profiledata.append(request.form["Value2"])
    profiledata.append(request.form["Value3"])
    profiledata.append(request.form["Value4"])
    profiledata.append(request.form["Value5"])
    profiledata.append(request.form["SelfAppearance"])
    profiledata.append(request.form["SelfSocial"])
    profiledata.append(request.form["SelfShy"])
    profiledata.append(request.form["SelfAlpha"])
    profiledata.append(request.form["SelfHumorous"])
    profiledata.append(request.form["SelfSpontaneous"])
    profiledata.append(request.form["SelfGenerous"])
    profiledata.append(request.form["SelfDriven"])
    profiledata.append(request.form["SelfIntuitive"])
    profiledata.append(request.form["SelfSexual"])
    profiledata.append(request.form["SelfOpenMinded"])
    profiledata.append(request.form["SelfVibe"])
    profiledata.append(request.form["SelfOvergiving"])
    profiledata.append(request.form["SelfDominant"])
    profiledata.append(request.form["Type1"])
    profiledata.append(request.form["Type2"])
    profiledata.append(request.form["Type3"])
    profiledata.append(request.form["Type4"])
    profiledata.append(request.form["Type5"])
    profiledata.append(request.form["S1_LogicVsFeelings"])
    profiledata.append(request.form["S1_QuitsVsStays"])
    profiledata.append(request.form["S1_PracticalVsEmotional"])
    profiledata.append(request.form["S1_CompatibilityVsChemistry"])
    profiledata.append(request.form["S2_ImprovementVsAcceptance"])
    profiledata.append(request.form["S2_ShortcomingsVSAcceptance"])
    profiledata.append(request.form["S3_SocialAcceptanceVsDontCare"])
    profiledata.append(request.form["S2_PickyVsPositives"])
    profiledata.append(request.form["S3_SocialAcceptanceVsDontCare"])
    profiledata.append(request.form["S3_SimilarVsDifferent"])
    profiledata.append(request.form["S4_LowStandardsVsHighStandards"])
    profiledata.append(request.form["S4_ImBetterVsMatch"])
    profiledata.append(request.form["S4_StayIfImBetterVsStayIfPartnerBetter"])

    print(profiledata)
    session.close()
    #db.session.add(profiles)
    #db.session.commit()
    return render_template("profile.html")





# @app.route("/formsubmit1", methods= ["POST", "GET"])
# def formsubmit1():
#     session = Session(engine)
#     agerange = request.form["AgeRange"]
#     gender = request.form["Gender"]
#     print(agerange)
#     print(gender)
#     session.close()

#     return render_template("profile.html")



if __name__ == "__main__":
    app.run(debug=True)



# value1 = request.form["Value1"]
# selfvalue1 = request.form["SelfValue1"]
# partnervalue1 = request.form["PartnerValue1"]
