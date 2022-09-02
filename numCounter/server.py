from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = '6d4c77de961d4a51425132516f452d2f8ef77566bd5ce136a7b21024f0ce90ef192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf' # set a secret key for security purposes

@app.route("/")
def index():
    if 'counter' not in session:
            session['counter'] = 0
    print("Contacting Index")
    return render_template("show.html")

@app.route('/route')
def count_up():
    session['counter'] += 1
    return redirect('/')

@app.route('/delete')
def delete():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)