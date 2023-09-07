import os
from flask import Flask, render_template, redirect,session,abort,request,url_for


app=Flask(__name__)
app.secret_key = "bc1qu6an3cmqsm9zn6plzg8xp7jc9yan4cn5jrv6lg"

users = {}

@app.get('/')
def home():
    return render_template('home.html', email=session.get("email"))


@app.get("/protected")
def protected():
    if not session.get("email"):
        abort(401)
    return render_template("protected.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if users.get(email) == password:
            session["email"] = email
            return redirect(url_for("protected"))
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        users[email] = password
        return redirect(url_for("login"))

    return render_template("signup.html")

