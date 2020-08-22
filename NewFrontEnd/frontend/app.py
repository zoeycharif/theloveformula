# import Libraries/Dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, render_template, jsonify, redirect, request, url_for, session, flash
from datetime import timedelta

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
app.secret_key = "hihi"
# app.permanent_session_lifetime = timedelta(days=1)

#################################################
# Database Setup
#################################################

# from flask_sqlalchemy import SQLAlchemy
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
    

@app.route("/ratings")
def ratings():
    return render_template("rating.html")


@app.route("/formsubmit", methods= ["POST", "GET"])
def formsubmit():
    session = Session(engine)
    results = session.query(Profiles.qp_communication).all()
    print(results)
    value1 = request.form["Value1"]
    selfvalue1 = request.form["SelfValue1"]
    partnervalue1 = request.form["PartnerValue1"]
    value2 = request.form["Value2"]
    selfvalue2 = request.form["SelfValue2"]
    partnervalue2 = request.form["PartnerValue2"]
    value3 = request.form["Value3"]
    selfvalue3 = request.form["SelfValue3"]
    partnervalue3 = request.form["PartnerValue3"]
    value4 = request.form["Value4"]
    selfvalue4 = request.form["SelfValue4"]
    partnervalue4 = request.form["PartnerValue4"]
    value5 = request.form["Value5"]
    selfvalue5 = request.form["SelfValue5"]
    partnervalue5 = request.form["PartnerValue5"]
    type1 = request.form["Type1"]
    partnertype1 = request.form["PartnerType1"]
    type1 = request.form["Type1"]
    partnertype1 = request.form["PartnerType1"]
    type2 = request.form["Type2"]
    partnertype2 = request.form["PartnerType2"]
    type3 = request.form["Type3"]
    partnertype3 = request.form["PartnerType3"]
    type4 = request.form["Type4"]
    partnertype4 = request.form["PartnerType4"]
    type5 = request.form["Type5"]
    partnertype5 = request.form["PartnerType5"]
    # logicVfeelings = request.form["S1_logicvsfeelings"]
    # quitsVstays = request.form["S1_QuitsVsStays"]
    # practicalVemotional = request.form["S1_PracticalVsEmotional"]
    # compVchem = request.form["S1_CompatibilityVsChemistry"]
    # improVaccept = request.form["S2_ImprovementVsAcceptance"]
    # shortVaccept = request.form["S2_ShortcomingsVSAcceptance"]
    # pickyVpost = request.form["S2_PickyVsPositives"]
    # socialVdontcare = request.form["S3_SocialAcceptanceVsDontCare"]
    # similarVdiff = request.form["S3_SimilarVsDifferent"]
    # lowsVhighs = request.form["S4_LowStandardsVsHighStandards"]
    # betterVmatch = request.form["S4_ImBetterVsMatch"]
    # staymeVstaypartner = request.form["S4_StayIfImBetterVsStayIfPartnerBetter"]
    print (value1)
    print (selfvalue1)
    print (partnervalue1)
    session.close()
    #db.session.add(profiles)
    #db.session.commit()
    return render_template("rating.html")


@app.route("/profile")
def profile():

    return render_template("profile.html")

@app.route("/personality", methods=["GET", "POST"])
def personality():

    return render_template("personality.html")

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




  
