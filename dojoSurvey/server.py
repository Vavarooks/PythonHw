from flask import Flask, render_template, redirect, request,session
app = Flask(__name__)
app.secret_key= "fbf39c81480360ef27f02ab33493e44d0965467ce8d5243786e4f57c68045d2d192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf"

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
    session ['name'] = request.form["name"]
    session ['location'] = request.form["location"]
    session ['coding'] = request.form["coding"]
    session ['text'] = request.form["text"]
    return redirect("/result")

@app.route("/result")
def result():

    print('Submitted Form')
    return render_template('result.html')

@app.route("/back")
def back():
    print('Go Back')
    return redirect("/works")

if __name__ == "__main__":
    app.run(debug = True)