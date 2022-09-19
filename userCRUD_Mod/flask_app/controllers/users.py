from flask_app import app
from flask import Flask, render_template, redirect, request, session, flash
from flask_app.models.user import Users

@app.route("/")
def index():
    all_users = Users.get_all()
    return render_template("read.html", all_users=all_users)

@app.route("/users/create")
def create_form():
    return render_template("create.html")

@app.route("/users/submit", methods=["post"])
def submit_user():
    print(request.form)

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }

    Users.save(data)

    return redirect("/")

@app.route("/users/<int:id>")
def single_user_page(id):
    data = {
        "id" : id
    }

    single_user = Users.get_one(data)
    return render_template("single_user.html", single_user=single_user)

@app.route("/delete/<int:id>")
def delete(id):
    data = {
        "id" : id
    }

    Users.delete(data)
    return redirect("/")

@app.route("/change/<int:id>")
def change_info(id):
    data = {
        "id" : id
    }
    single_user = Users.get_one(data)
    return render_template("update.html", single_user=single_user)

@app.route("/edited/<int:id>", methods=["post"])
def edited(id):
    data ={
        "id" : id,
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    Users.edit(data)
    print("Edit")
    return redirect("/")
