from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route("/")
def defaultPage():
    return '<h1>Search for Page after /</h1>'

@app.route("/register", methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        output = request.form
        return render_template("result.html", result = output)
    else:
        return render_template("Registration.html")

if __name__ == '__main__':
    app.run(debug = True)
    