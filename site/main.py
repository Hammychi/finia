from distutils.log import debug
from flask import Flask, redirect, url_for, render_template, request
from requests import get
app = Flask(__name__)

@app.route("/")
def home():
    ip = get('https://api.ipify.org').text
    return render_template("index.html", chad=ip)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == '__main__':
    app.run(debug=True)
    