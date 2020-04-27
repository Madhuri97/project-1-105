import os
from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, redirect, url_for, render_template, request, session
import logging
from Schema import *
from books_db import *
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db.init_app(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
# Session = scoped_session(sessionmaker(bind=engine))
# session = Session()

#set up routes
@app.route("/")
@app.route("/register", methods = ['POST', 'GET'])
def result():
    db.create_all()
    if request.method == 'POST':
        udata = schema(request.form["name"], request.form["email"], request.form["pswd"])
        user = schema.query.filter_by(email = request.form['email']).first()
        if user is not None:
            print("User already exists. try to register if you are new user")
            var = "User already exists. please try to register if you are a new user"
            return render_template("Registration.html", message1 = var)
        db.session.add(udata)
        db.session.commit()
        var = 'Registration is successful'
        return render_template("Registration.html", message = var)   
    else:
        return render_template("Registration.html")

@app.route('/admin')
def admin():
    alludata = schema.query.order_by(desc(schema.createtimestamp)).all()
    return render_template("admin.html", admin = alludata)

@app.route('/authen', methods = ['POST'])
def login():
    user = schema.query.filter_by(email = request.form['email']).first()
    if user is not None:
        if  request.form["pswd"] == user.pwd:
            session['email'] = request.form['email']
            print(session)
            return redirect('/home')
        else:
            print("Wrong credentials")
            var = "Wrong Cresdentials" 
            return render_template("Registration.html", message1 = var)
    else:
        print("You are not registered user, Please first register to login")
        var = "You are not a registered user, Please first register to login"
        return render_template("Registration.html", message1 = var)

@app.route("/home")
def home():
    try: 
        user = session['email']
        return render_template("login.html")
    except:
        var = "You must login to view the homepage"
        return render_template("Registration.html", message1 = var)

@app.route("/logout")
def logout():
    try: 
        session.clear()
        var = "Logged Out"
        return render_template("Registration.html", message1 = var)
    except:
        var = "You must logout from the page"
        return render_template("Registration.html", message1 = var)

@app.route("/bookpage/<id>")
def bookpage(id):
    booksdata = db.session.query(Books).filter(Books.isbn == id)
    return render_template("bookpage.html", data = booksdata)