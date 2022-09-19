from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import Users
from flask import Flask, render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from flask_app import app
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["post"])
def register_user():
    print("trying to register here")
    print(request.form)

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": request.form["password"],
        "password_confirm": request.form["password_confirm"],
    }

    if not Users.validate(data):
        print("not valid")
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data["password"] = pw_hash
    print(f"password:{request.form['password']}")
    
    user_id = Users.save(data)
    session["logged_id"] = user_id
    return redirect('/success')

@app.route("/success")
def success():
    if "logged_id" not in session:
        return redirect("/")
    return render_template("success.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/login", methods=["post"])
def login():

    data = {
        "email" : request.form["email"]
    }

    this_user = Users.find_one_by_email(data)

    if not this_user:
        flash("Invalid Email or Password")
        return redirect("/")
    if not bcrypt.check_password_hash(this_user.password, request.form['password']):
        flash("Invalid Email or Password")
        return redirect("/")

    session["logged_id"] = this_user.id
    
    print("Successful Login!")


    return redirect("/success")