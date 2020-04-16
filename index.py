from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

@app.route("/")
@app.route("/register", methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        output = request.form
        print(output['name'])
        return render_template("result.html", result = output)   
    else:
        return render_template("Registration.html")

if __name__ == '__main__':
    app.run(debug = True)
    