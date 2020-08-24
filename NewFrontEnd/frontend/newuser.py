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

URI = "postgres://rhjtenpwhdlbjl:4d3153a71d04ee752de8aab6fb6ac3baaff5fe615aa7a6223845aab661e0c6af@ec2-34-237-89-96.compute-1.amazonaws.com:5432/d1l8p7t7cs19l8"

engine = create_engine(URI)

session = Session(engine)
inspector = inspect(engine)
columns = inspector.get_columns("profiles")
#for c in columns:
    #print(c["name"])
#Base = automap_base()
#Base.prepare(engine, reflect = True)
#print(Base.classes.keys())
#Profiles = Base.classes.profiles


# select username from profile where username = x
session.query(profiles.username)

# create route that renders newuser.html template
@app.route("/")
def home():

    return render_template("newuser.html")

@app.route("/formsubmit1", methods= ["POST", "GET"])
def formsubmit1():

