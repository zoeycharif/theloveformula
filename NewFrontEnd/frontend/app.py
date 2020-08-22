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
    # print (selfvalue1)
    # print (partnervalue1)
    session.close()
    #db.session.add(profiles)
    #db.session.commit()
    return render_template("rating.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/formsubmit1", methods= ["POST", "GET"])
def formsubmit1():
    session = Session(engine)
    results = session.query(Profiles.qp_communication).all()
    print(results)
    profiledata = []
    profiledata.append(request.form["AgeRange"])
    # profiledata.append(request.form["Gender"])
    # profiledata.append(request.form["Orientation"])
    # profiledata.append(request.form["CurrentStatus"])
    # profiledata.append(request.form["TogetherTime"])
    # profiledata.append(request.form["RelationshipDescription"])
    # profiledata.append(request.form["Value1"])
    # profiledata.append(request.form["SelfValue1"])
    # profiledata.append(request.form["PartnerValue1"])
    # profiledata.append(request.form["Value2"])
    # profiledata.append(request.form["SelfValue2"])
    # profiledata.append(request.form["PartnerValue2"])
    # profiledata.append(request.form["Value3"])
    # profiledata.append(request.form["SelfValue3"])
    # profiledata.append(request.form["PartnerValue3"])
    # profiledata.append(request.form["Value4"])
    # profiledata.append(request.form["SelfValue4"])
    # profiledata.append(request.form["PartnerValue4"])
    # profiledata.append(request.form["Value5"])
    # profiledata.append(request.form["SelfValue5"])
    # profiledata.append(request.form["PartnerValue5"])
    # profiledata.append(request.form["Type1"])
    # profiledata.append(request.form["PartnerType1"])
    # profiledata.append(request.form["Type2"])
    # profiledata.append(request.form["PartnerType2"])
    # profiledata.append(request.form["Type3"])
    # profiledata.append(request.form["PartnerType3"])
    # profiledata.append(request.form["Type4"])
    # profiledata.append(request.form["PartnerType4"])
    # profiledata.append(request.form["Type5"])
    # profiledata.append(request.form["PartnerType5"])

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



# value1 = request.form["Value1"]
# selfvalue1 = request.form["SelfValue1"]
# partnervalue1 = request.form["PartnerValue1"]
  
