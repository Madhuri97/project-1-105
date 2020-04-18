import os
from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, redirect, url_for, render_template, request, session
from Schema import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db.init_app(app)
# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
Session = scoped_session(sessionmaker(bind=engine))
session = Session()
@app.route("/")
@app.route("/register", methods = ['POST', 'GET'])
def result():
    db.create_all()
    if request.method == 'POST':
        udata = schema(request.form["name"], request.form["email"], request.form["pswd"])
        user = schema.query.filter_by(email = request.form['email']).first()
        if user is not None:
            print("User already exists. try to register if you are new user")
            var = "Error: User already exists. please try to register if you are a new user"
            return render_template("Registration.html", message1 = var)
        # output = request.form
        # print(output['name'])
        db.session.add(udata)
        db.session.commit()
        var = 'Registration Success'
        return render_template("Registration.html", message = var)   
    else:
        return render_template("Registration.html")


@app.route('/admin')
def admin():
    alludata = schema.query.all()
    return render_template("admin.html", admin = alludata)



# creation of table

# if __name__ == '__main__':
#     # db.create_all()
#     app.run(debug = True)
    