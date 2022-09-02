from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    print("Contacting Index")
    return("Hello World!")

# @app.route("/repeat/<phrase>/<int:times>")
# def repeat_phrase(phrase, times):
#     repeated = phrase * times
#     return repeated

@app.route("/multi")
def multi():
    return render_template("index.html", phrase="hello", times=5)	# notice the 2 new named arguments!

@app.route("/works")
def works():
    print("Work")
    return render_template('basic.html')

# @app.route("/main")
#     def main():
#         print("Hello")

@app.route("/play/<int:times>")
def play(times):
    return render_template("index.html",times=times)

@app.route("/change/<color>/<int:times>")
def change(color,times):
    return render_template("colors.html",color=color, times=times)

if __name__ == "__main__":
    app.run(debug = True)