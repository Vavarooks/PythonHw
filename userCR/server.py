from flask import Flask, render_template, redirect, request
app = Flask(__name__)
from users import Users

@app.route("/")
def index():
    all_users = Users.get_all()
    print(all_users)
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
        "email": request.form["email"],
    }

    Users.save(data)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)