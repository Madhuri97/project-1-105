from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
def defaultPage():
    return '<h1>Search for Page after /</h1>'

@app.route("/register")
def result():
        return render_template("Registration.html")

