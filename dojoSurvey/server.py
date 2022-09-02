from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route("/")
def index():
    print("Contacting Index")
    return("Hello World!")

@app.route("/works")
def works():
    print("Work")
    return render_template('index.html')

@app.route("/process", methods=["post"])
def process():
    print(request.form["name"])
    print(request.form["location"])
    print(request.form["coding"])
    print(request.form["text"])
    return redirect("/result")

@app.route("/result")
def result():
    print('Submitted Form')
    return render_template('result.html')

@app.route("/back")
def back():
    print('Go Back')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True)