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
    return render_template("form2.html")


    # return render_template("index.html")
    
@app.route("/form", methods=["GET", "POST"])
def form():
    # if request.method == "POST":

    return render_template("form.html")

@app.route("/formsubmit", methods= ["POST"])
def formsubmit():
    session = Session(engine)
    results = session.query(Profiles.qp_communication).all()
    print(results)
    selfvalue1 = request.form["selfvalue1"]
    print (selfvalue1)
    session.close()
    return render_template("form2.html")

# Query the database and send the jsonified results
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # session.permanent = True
        user = request.form["namo"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("you have been logged out ")
    return redirect(url_for("login"))
        

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)




# @app.route("api/loveequation")
# def loveequation():
#     results = db.session.query(user.UserName, user.Pword, user.UserNumber).all()
#     data = []
#     for i in results:
#         data.append(i) 
  
#     loveequation_data = [{

#     }]
    
#     return jsonify()
    
    
    # if __name__ == "__main__":
    # app.run(debug=True)


  
