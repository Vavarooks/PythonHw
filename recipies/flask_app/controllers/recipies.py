from flask_app.models.recipie import Recipies
from flask_app.models.user import Users
from flask import Flask, render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from flask_app import app
bcrypt = Bcrypt(app)

@app.route("/")
def home():
    all_recipies = Recipies.get_all()
    return render_template("home.html", all_recipies=all_recipies)

@app.route("/form")
def recipe_form():
    return render_template("form.html")

@app.route("/main")
def userIn():
    all_recipies = Recipies.get_all()
    return render_template("loggedin.html", all_recipies=all_recipies)

@app.route("/pantry/<int:id>")
def veiw_one(id):
    data = {
        "id" : id,
    }
    if "logged_id" not in session:
        flash("Log in to veiw!")
        return redirect("/")
    one_recipies = Recipies.veiw_one(data)
    userid = {
        "id": Recipies.users_id
    }
    operator = {
        "id": session["logged_id"]
    }
    this_user = Users.find_one_by_id(operator)
    posted_by_this_user = Users.find_one_by_id(userid)
    print(one_recipies)
    return render_template("recipeveiw.html", one_recipies=one_recipies,this_user = this_user, posted_by_this_user = posted_by_this_user)

@app.route("/recipies/submit", methods=["post"])
def submit_recipie():
    print(request.form)

    data = {
        "name" : request.form["name"],
        "instructions" : request.form["instructions"],
        "nutrients" : request.form["nutrients"],
        "cook" : request.form["cook"],
        "users_id" : session["logged_id"]
    }

    Recipies.save(data)

    return redirect("/main")

@app.route("/delete/<int:id>")
def delete(id):
    data = {
        "id" : id
    }

    Recipies.delete(data)
    return redirect("/main")

@app.route("/change/<int:id>")
def change_info(id):
    data = {
        "id" : id
    }
    change_recipe = Recipies.veiw_one(data)
    print(change_recipe)
    return render_template("edit.html", recipe=change_recipe)

@app.route("/edited", methods=["post"])
def edited():
    data ={
        "id": request.form["id"],
        "name" : request.form["name"],
        "instructions" : request.form["instructions"],
        "nutrients" : request.form["nutrients"],
        "cook" : request.form["cook"],
    }
    print("Edit")
    Recipies.edit(data)
    return redirect("/main")

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

    user_recipies = Recipies.veiw_one({"id": session["logged_id"]})
    # print(user_recipies)
    return render_template("success.html", user_recipies=user_recipies)

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



