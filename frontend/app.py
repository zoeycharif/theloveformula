# import Libraries/Dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, render_template, jsonify, redirect, request, url_for, session
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
# URI = "postgres://rhjtenpwhdlbjl:4d3153a71d04ee752de8aab6fb6ac3baaff5fe615aa7a6223845aab661e0c6af@ec2-34-237-89-96.compute-1.amazonaws.com:5432/d1l8p7t7cs19l8"

# engine = create_engine(URI)

# session = Session(engine)


# create route that renders index.html template
@app.route("/")
def home():

    return render_template("index.html")

@app.route("/form")
def form():

    return render_template("form.html")

# @app.route("/signup")
# def signup():
#     return render_template("signup.html")

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


  
