import os
from flask import Flask, session, redirect, jsonify
from flask_session import Session
from sqlalchemy import create_engine, desc, or_
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Flask, url_for, render_template, request, session
import logging
from Schema import *
from review import *
from books_db import *


logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# Check for environment variable
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db.init_app(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))

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
            return render_template("Registration.html", errormessage1 = var)
        db.session.add(userdata)
        db.session.commit()
        var = 'Registration is successful'
        return render_template("Registration.html", message = var)   
    else:
        return render_template("Registration.html")

#this is used to find whether the user is authenticated or not
@app.route('/authen', methods = ['POST'])
def login():
    user = schema.query.filter_by(email = request.form['email']).first()
    if user is not None:
        if  request.form["pswd"] == user.pwd:
            session['email'] = request.form['email']
            print(session)
            return redirect('/home')
        else:
            var = "Wrong Cresdentials" 
            return render_template("Registration.html",errormessage1 = var)
    else:
        print("You are not registered user, Please first register to login")
        var = "You are not a registered user, Please first register to login"
        return render_template("Registration.html", errormessage1 = var)

#this is used to get the search only after login
@app.route("/home", methods = ['POST', 'GET'])
def home():
    try: 
        user = session['email']
        if request.method == 'POST':
            req = request.form['Search']
            print(req)
            reqs = str(req)
            #partial search 
            booksdata = db.session.query(Books.isbn, Books.title, Books.author, Books.year).filter(or_(Books.title.like("%"+reqs+"%"), Books.author.like("%"+reqs+"%"), Books.isbn.like("%"+reqs+"%"))).all()
            if booksdata.__len__() == 0:
                var = "No search found!"
                return render_template("login.html", user = user, errormessage1 = var)
            return render_template("login.html", booksdata = booksdata, formaction = '/home', user = user)  
        return render_template("login.html", user =user)
    except Exception as e:
        print(e)
        var = "You must login to view the homepage"
        return render_template("Registration.html", errormessage1 = var)

#Bookpage route starts here
#get-renders bookpage, 
#Post-renders review.
@app.route("/bookpage/<id>", methods=[ 'POST', 'GET'])
def bookpage(id):
    # If the session has been created it goes to the try block
    try:
        user = session['email']
        print(user)
        if request.method == 'POST':   #If the method is post, which we get from the html page, it enters the block.
            r = reviews(id, user, request.form["rate"], request.form["review"]) #retrieving the data
            # data = reviews.query.filter_by(user = user, isbn = id).first() # It gets the user and Isbn from the form
            # print(temp)
            # details = reviews.query.all()
            booksdata = db.session.query(Books).filter(Books.isbn == id)
            details = db.session.query(reviews).filter(reviews.isbn == id, reviews.user == user).all() # It collects the data from database whose Isbn is equals to the submitted form isbn
            print(details)
            user_reviews = db.session.query(reviews).filter(reviews.isbn == id).all()
            if details.__len__() != 0: # checking whether the user name and isbn pair is in the data base, if the pair is already in the data base, it enters the block
                print("Sorry, You have already reviewed  book")
                error_message = "Error: Sorry, You have already reviewed  book"
                return render_template("bookpage.html", error_message  = error_message, details = details, user_reviews = user_reviews, data = booksdata) #returning error message and table data to the review page.
            print(r)
            db.session.add(r) #adding data to the database
            db.session.commit()
            booksdata = db.session.query(Books).filter(Books.isbn == id)
            details = db.session.query(reviews).filter(reviews.isbn == id, reviews.user == user).all() # It collects the data from database whose Isbn is equals to the submitted form isbn
            user_reviews = db.session.query(reviews).filter(reviews.isbn == id).all()
            success_message = "Thank you for reviewing the book"
            return render_template("bookpage.html", success_message = success_message, details=details, user_reviews = user_reviews, data = booksdata)
        else:
            details = db.session.query(reviews).filter(reviews.isbn == id, reviews.user == user).all()
            booksdata = db.session.query(Books).filter(Books.isbn == id)
            user_reviews = db.session.query(reviews).filter(reviews.isbn == id).all()
            return render_template("bookpage.html", data = booksdata, details= details, user_reviews = user_reviews)
    except Exception as e:
        print(e)
        #if the session is not created, it goes to the registration page for starting the session.
        var = "You must login to view the homepage"
        return render_template("Registration.html", message = var)
#This route ends here


#route after logout is done by the user
@app.route("/logout")
def logout():
    try: 
        session.clear()
        var = "Logged Out"
        return render_template("Registration.html", message = var)
    except:
        var = "You must logout from the page"
        return render_template("Registration.html", message1 = var)


# Third route -- Review submission
@app.route('/api/submitReview', methods  =['POST'])
def submitreview():
    if not request.is_json:
        message = "Invalid request format"
        # print("here1");
        return jsonify(message),400
    isbn = request.args.get("isbn")
    try:
        result = db.session.query(Books).filter(Books.isbn == isbn).first()
    except:
        message = "Please Try again Later"
        return jsonify(message),500
    if result is None:
        print("here");
        message = "Please enter valid ISBN"
        return jsonify(message), 404
    rate = request.get_json()['rate']
    review = request.get_json()['review']
    email = request.get_json()['email']
    user = reviews.query.filter_by(user=email,isbn=isbn).first()
    if user is not None:
        message = "Sorry you can't review this book again"
        return jsonify(message), 409
    reviewdata=reviews(isbn,email,rate,review)
    try:
        db.session.add(reviewdata)
        db.session.commit()
    except:
        message = "Please Try Again "
        return jsonify(message), 500
    # print(isbn,rating,comment)
    message = "Review submitted successfully"
    return jsonify(message), 200

# start of book api route
@app.route('/api/book')
def apibook():
    query = request.args.get('isbn')
    print(query)
    try:
        booksdata = db.session.query(Books).filter(Books.isbn == query).first()
        details = db.session.query(reviews).filter(reviews.isbn == query).all() 
    except Exception as e:
        print(e)
        message = "Please try again"
        return jsonify(message),500
    if booksdata is None:
        message = "No book found"
        return jsonify(message), 404
    response = {}
    reviewss= []
    print(reviewss)
    for review in details:
        eachreview = {}
        eachreview["email"] = review.user
        eachreview["rate"] = review.rate
        eachreview["review"] = review.review
        reviewss.append(eachreview)
    response["isbn"] = booksdata.isbn
    response["title"] = booksdata.title
    response["author"] = booksdata.author
    response["year"] = booksdata.year
    response["reviews"] = reviewss
    print(response)
    return jsonify(response),200
# end of the book api route

#route admin
@app.route('/admin')
def admin():
    alludata = schema.query.order_by(desc(schema.createtimestamp)).all()
    return render_template("admin.html", admin = alludata)

#Json api route 
@app.route('/api/search', methods = ["POST"])
def apiSearch():
    if not request.is_json:
        message = "Invalid request format"
        return jsonify(message), 400
    reqs = request.get_json()['query']
    try:
        booksdata = db.session.query(Books.isbn, Books.title, Books.author, Books.year).filter(or_(Books.title.like("%"+reqs+"%"), Books.author.like("%"+reqs+"%"), Books.isbn.like("%"+reqs+"%"))).all()
    except: 
        message = "Please Try again Later"
        return jsonify(message), 500
    if booksdata.__len__() == 0:
        message = "No search results found"
        return jsonify(message),404
    response = []
    for book in booksdata:
        dictionary = {}
        dictionary["isbn"] = book[0]
        dictionary["title"] = book[1]
        dictionary["author"] = book[2]
        dictionary["year"] = book[3]
        response.append(dictionary)
    return jsonify(response), 200


