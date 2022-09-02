from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    print("Contacting Index")
    return("Hello World!")

@app.route("/works")
def works():
    print("Work")
    return render_template('index.html')

@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
        
    ]
    return render_template("index.html", users = users)

if __name__ == "__main__":
    app.run(debug = True)