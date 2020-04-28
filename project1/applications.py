import os
from flask import Flask, session, redirect
from flask_session import Session
from sqlalchemy import create_engine, desc, or_
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, url_for, render_template, request, session
import logging
from Schema import *
from books_db import Books

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# Check for environment variable
# if not os.getenv("DATABASE_URL"):
#     raise RuntimeError("DATABASE_URL is not set")

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
        userdata = schema(request.form["name"], request.form["email"], request.form["pswd"])
        user = schema.query.filter_by(email = request.form['email']).first()
        if user is not None:
            print("User already exists. try to register if you are new user")
            var = "User already exists. please try to register if you are a new user"
            return render_template("Registration.html", message1 = var)
        db.session.add(userdata)
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

@app.route("/home", methods = ['POST', 'GET'])
def home():
    try: 
        user = session['email']
        if request.method == 'POST':
            req = request.form['Search']
            print(req)
            reqs = str(req)
            booksdata = db.session.query(Books.isbn, Books.title, Books.author, Books.year).filter(or_(Books.title.like("%"+reqs+"%"), Books.author.like("%"+reqs+"%"), Books.isbn.like("%"+reqs+"%"))).all()
            if booksdata.__len__() == 0:
                var = "No search found!"
                return render_template("login.html", user = user, message1 = var)
            return render_template("login.html", booksdata = booksdata, formaction = '/home', user = user)  
        return render_template("login.html", user =user)
    except Exception as e:
        print(e)
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
