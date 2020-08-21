import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

# from flask_sqlalchemy import SQLAlchemy
URI = "postgres://rhjtenpwhdlbjl:4d3153a71d04ee752de8aab6fb6ac3baaff5fe615aa7a6223845aab661e0c6af@ec2-34-237-89-96.compute-1.amazonaws.com:5432/d1l8p7t7cs19l8"

engine = create_engine(URI)

session = Session(engine)


# create route that renders index.html template
@app.route("/")
def home():

    return render_template("index.html")


# Query the database and send the jsonified results
@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        age = request.form[""]

    return render_template("form.html")

@app.route("api/loveequation")
def loveequation():
    results = db.session.query(user.UserName, user.Pword, user.UserNumber).all()
    data = []
    for i in results:
        data.append(i) 
  
    loveequation_data = [{

    }]
    

    return jsonify()
    
    
    if __name__ == "__main__":
    app.run(debug=True)


  
